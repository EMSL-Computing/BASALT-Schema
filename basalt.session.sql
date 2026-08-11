-- Total row count and basic statistics
SELECT 
    COUNT(*) AS total_links,
    COUNT(DISTINCT processing_id) AS unique_processes,
    COUNT(DISTINCT sample_base_id) AS unique_samples,
    AVG(links_per_process) AS avg_links_per_process
FROM public."processingSampleLink"
CROSS JOIN LATERAL (
    SELECT COUNT(*) AS links_per_process
    FROM public."processingSampleLink" psl2
    WHERE psl2.processing_id = public."processingSampleLink".processing_id
) sub;

-- Samples involved in multiple processes (reuse patterns)
SELECT 
    sample_base_id,
    COUNT(DISTINCT processing_id) AS process_count,
    ARRAY_AGG(DISTINCT role ORDER BY role) AS roles_used
FROM public."processingSampleLink"
GROUP BY sample_base_id
HAVING COUNT(DISTINCT processing_id) > 1
ORDER BY process_count DESC
LIMIT 20;

-- Samples with multiple steps in same process (workflow chains)
SELECT 
    sample_base_id,
    processing_id,
    COUNT(DISTINCT step_number) AS step_count,
    ARRAY_AGG(step_number ORDER BY step_number) AS steps,
    ARRAY_AGG(role ORDER BY step_number) AS step_roles
FROM public."processingSampleLink"
GROUP BY sample_base_id, processing_id
HAVING COUNT(DISTINCT step_number) > 1
LIMIT 20;

-- Distribution of samplerole values
SELECT 
    role,
    COUNT(*) AS usage_count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS percentage
FROM public."processingSampleLink"
GROUP BY role
ORDER BY usage_count DESC;

-- Step number patterns for top 5 processes
WITH top_processes AS (
    SELECT processing_id, COUNT(*) AS link_count
    FROM public."processingSampleLink"
    GROUP BY processing_id
    ORDER BY link_count DESC
    LIMIT 5
)
SELECT 
    psl.processing_id,
    sp.method_name,
    psl.step_number,
    psl.role,
    COUNT(*) AS samples_at_step
FROM public."processingSampleLink" psl
JOIN top_processes tp ON psl.processing_id = tp.processing_id
LEFT JOIN public."sampleProcessing" sp ON psl.processing_id = sp.id
GROUP BY psl.processing_id, sp.method_name, psl.step_number, psl.role
ORDER BY psl.processing_id, psl.step_number, psl.role;


-- Confirm table structure and relationships
SELECT 
    sb.id AS sample_base_id,
    sb.sample_base_type,
    s.id AS sample_id,
    s.type AS sample_type,
    ps.id AS processed_sample_id,
    ps.processed_sample_type
FROM public."sampleBase" sb
LEFT JOIN sample s ON s.id = sb.id
LEFT JOIN public."processedSample" ps ON ps.id = sb.id
LIMIT 10;

-- Check processingSampleLink coverage for processed samples
SELECT 
    ps.processed_sample_type,
    COUNT(DISTINCT ps.id) AS total_processed_samples,
    COUNT(DISTINCT psl.sample_base_id) AS samples_with_links,
    ROUND(100.0 * COUNT(DISTINCT psl.sample_base_id) / COUNT(DISTINCT ps.id), 2) AS coverage_pct
FROM public."processedSample" ps
LEFT JOIN public."processingSampleLink" psl ON psl.sample_base_id = ps.id
GROUP BY ps.processed_sample_type;