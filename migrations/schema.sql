-- # Class: "study" Description: ""
--     * Slot: id Description: 
--     * Slot: participant_name Description: 
--     * Slot: principal_investigator Description: 
--     * Slot: collaborating_institution Description: 
--     * Slot: project_status Description: 
--     * Slot: project_start Description: 
--     * Slot: project_end Description: 
--     * Slot: proposal_title Description: 
--     * Slot: proposal_abstract Description: 
--     * Slot: project_id Description: 
-- # Class: "samplingActivity" Description: ""
--     * Slot: id Description: 
--     * Slot: study_id Description: 
--     * Slot: type Description: 
--     * Slot: sample_name Description: 
--     * Slot: lims_barcode Description: 
--     * Slot: alt_id Description: 
--     * Slot: elev_id Description: 
--     * Slot: lat_lon_id Description: 
--     * Slot: growth_facil Description: 
--     * Slot: other_growth_facil Description: 
--     * Slot: other_storage_condt Description: 
--     * Slot: oxygen_relationship Description: 
--     * Slot: sample_store_temp Description: 
--     * Slot: samp_biotic_relationship Description: 
--     * Slot: storage_condt Description: 
--     * Slot: air_temp_regm Description: 
--     * Slot: chem_administration Description: 
--     * Slot: collection_date Description: 
--     * Slot: collection_time Description: 
--     * Slot: env_broad_scale_other Description: 
--     * Slot: env_local_scale_other Description: 
--     * Slot: env_medium_other Description: 
--     * Slot: experimental_factor Description: 
--     * Slot: experimental_factor_other Description: 
--     * Slot: extraction_method Description: 
--     * Slot: extreme_event Description: 
--     * Slot: gaseous_environment Description: 
--     * Slot: geo_loc_name Description: 
--     * Slot: humidity_regm Description: 
--     * Slot: isotope_exposure Description: 
--     * Slot: light_regm Description: 
--     * Slot: link_addit_analys Description: 
--     * Slot: method_development Description: 
--     * Slot: microbial_biomass_c_meth Description: 
--     * Slot: microbial_biomass_meth Description: 
--     * Slot: microbial_biomass_n_meth Description: 
--     * Slot: misc_param Description: 
--     * Slot: neon_plot_id Description: 
--     * Slot: non_microb_biomass_method Description: 
--     * Slot: other_sample_store_temp Description: 
--     * Slot: other_treatment Description: 
--     * Slot: ph Description: 
--     * Slot: ph_meth Description: 
--     * Slot: salinity Description: 
--     * Slot: salinity_method Description: 
--     * Slot: sample_collected Description: 
--     * Slot: sample_collection_dev Description: 
--     * Slot: sample_collection_method Description: 
--     * Slot: sample_end_time Description: 
--     * Slot: sample_processing Description: 
--     * Slot: sample_start_time Description: 
--     * Slot: season_environment Description: 
--     * Slot: shipped_sample_size Description: 
--     * Slot: sieving Description: 
--     * Slot: start_date_inc Description: 
--     * Slot: tot_nitro_cont_meth Description: 
--     * Slot: tot_org_c_meth Description: 
--     * Slot: watering_regm Description: 
-- # Class: "sampleBase" Description: ""
--     * Slot: id Description: 
--     * Slot: sample_name Description: The human readable name for the sample
--     * Slot: proposal_id Description: The 5 digit project ID assigned to an EMSL user proposal/project
--     * Slot: sampling_set Description: 
--     * Slot: sample_base_type Description: The name of the sample set if the sample is a part of a set of samples processed together
-- # Class: "sample" Description: "A physical sample collected from the environment"
--     * Slot: id Description: 
--     * Slot: sampling_activity_id Description: Reference to the sampling activity that collected this sample
--     * Slot: type Description: The type of sample (soil, aerosol, etc.)
--     * Slot: guid_source Description: Indicate the source of the GUID that you have provided for your samples
--     * Slot: other_guid_source Description: Please specify if other GUID source
-- # Class: "soil_sample" Description: "A soil sample with specific soil-related properties"
--     * Slot: id Description: 
--     * Slot: soil_type Description: The specific type of soil sample
-- # Class: "aerosol_sample" Description: "An aerosol sample with specific aerosol-related properties"
--     * Slot: id Description: 
--     * Slot: aerosol_type Description: The type or method of aerosol collection
-- # Class: "processedSample" Description: "A sample that has undergone processing or analysis"
--     * Slot: id Description: 
--     * Slot: processed_sample_type Description: The type of processed sample
-- # Class: "coreSection" Description: "A section of a core sample (TOP, MID, BTM)"
--     * Slot: id Description: 
--     * Slot: core_section Description: The section of the core (e.g. TOP, MID, BTM)
-- # Class: "replicate" Description: "A replicate or aliquot of a sample"
--     * Slot: id Description: 
--     * Slot: rep Description: The replicate (or aliquot) number
-- # Class: "processedData" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: name Description: 
--     * Slot: proposal_id Description: 
--     * Slot: sampling_set Description: 
--     * Slot: core_section Description: 
--     * Slot: sample_name Description: 
--     * Slot: s3_base_url Description: 
--     * Slot: s3_bucket Description: 
--     * Slot: s3_key Description: 
--     * Slot: filesize Description: 
--     * Slot: md5checksum Description: 
--     * Slot: workflow_id Description: 
--     * Slot: lims_barcode Description: 
--     * Slot: version Description: 
-- # Class: "analysisActivity" Description: ""
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: analyte_id Description: 
--     * Slot: name Description: 
--     * Slot: acquisition_time Description: 
--     * Slot: instrument_id Description: 
--     * Slot: protocol_url Description: 
--     * Slot: instrument_operator_id Description: 
--     * Slot: version Description: 
-- # Class: "instrumentData" Description: ""
--     * Slot: id Description: 
--     * Slot: analysis_activity_id Description: 
--     * Slot: description Description: 
--     * Slot: alternative_identifiers Description: 
--     * Slot: compression_type Description: 
--     * Slot: file_size_bytes Description: 
--     * Slot: md5_checksum Description: 
--     * Slot: name Description: 
--     * Slot: type Description: 
--     * Slot: url Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: file_type Description: 
--     * Slot: version Description: 
-- # Class: "workflowExecutionActivity" Description: ""
--     * Slot: id Description: 
--     * Slot: raw_data_id Description: 
--     * Slot: description Description: 
--     * Slot: ended_at_time Description: 
--     * Slot: git_url Description: 
--     * Slot: name Description: 
--     * Slot: started_at_time Description: 
--     * Slot: type Description: 
--     * Slot: used_id Description: 
--     * Slot: execution_resource Description: 
--     * Slot: workflow_steps Description: 
--     * Slot: version Description: 
-- # Class: "alternativeIdentifier" Description: ""
--     * Slot: id Description: 
--     * Slot: alternate_id Description: 
--     * Slot: alternate_identifier_type Description: 
-- # Class: "ecoregion" Description: ""
--     * Slot: domain_id Description: 
--     * Slot: domain_name Description: 
-- # Class: "functionalAnnotationIdentifier" Description: ""
--     * Slot: id Description: 
--     * Slot: functional_identifier Description: 
--     * Slot: database Description: 
-- # Class: "instrument" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: alternative_names Description: 
--     * Slot: vendor Description: 
--     * Slot: model Description: 
--     * Slot: instrument_parameters Description: 
-- # Class: "metaboliteQuantification" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: alternative_identifiers Description: 
--     * Slot: highest_similarity_score Description: 
--     * Slot: metabolite_quantified Description: 
-- # Class: "ontologyClass" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: alternative_identifiers Description: 
--     * Slot: name Description: 
-- # Class: "peptideQuantification" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: all_proteins Description: 
--     * Slot: best_protein Description: 
--     * Slot: min_q_value Description: 
--     * Slot: peptide_sequence Description: 
--     * Slot: peptide_spectral_count Description: 
--     * Slot: peptide_sum_masic_abundance Description: 
-- # Class: "zipDownload" Description: ""
--     * Slot: id Description: 
--     * Slot: time Description: 
--     * Slot: user Description: 
--     * Slot: files Description: 
--     * Slot: packages Description: 
-- # Class: "containerType" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: container_type Description: 
--     * Slot: container_size_id Description: 
-- # Class: "custodian" Description: ""
--     * Slot: id Description: 
--     * Slot: person_id Description: 
-- # Class: "instrument_alt_id" Description: ""
--     * Slot: id Description: 
--     * Slot: instrument_alt_id_provider Description: 
--     * Slot: instrument_id Description: 
-- # Class: "labDevice" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: device_type Description: 
--     * Slot: activity_time_id Description: 
--     * Slot: activity_speed_id Description: 
-- # Class: "sampleProcessing" Description: ""
--     * Slot: id Description: 
--     * Slot: analysis_type Description: 
--     * Slot: method_name Description: 
--     * Slot: processing_steps Description: 
--     * Slot: url Description: 
--     * Slot: version Description: 
-- # Class: "processingSampleLink" Description: ""
--     * Slot: id Description: 
--     * Slot: sample_base_id Description: 
--     * Slot: processing_id Description: 
--     * Slot: step_number Description: 
--     * Slot: role Description: 
--     * Slot: version Description: 
-- # Class: "instrumentCustodian" Description: ""
--     * Slot: id Description: 
--     * Slot: instrument_id Description: 
--     * Slot: custodian_id Description: 
-- # Class: "workflowExecutionFunctionalAnnotation" Description: ""
--     * Slot: id Description: 
--     * Slot: workflow_id Description: 
--     * Slot: functional_annotation_id Description: 
--     * Slot: count Description: 
-- # Class: "timestampValue" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: has_raw_value Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
-- # Class: "textValue" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: language Description: 
--     * Slot: has_raw_value Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
-- # Class: "softwareControlledTermValue" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: name Description: 
--     * Slot: version Description: 
--     * Slot: has_raw_value Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: type Description: 
-- # Class: "controlledTermValue" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: has_raw_value Description: 
--     * Slot: was_generated_by Description: 
--     * Slot: type Description: 
-- # Class: "personValue" Description: ""
--     * Slot: email Description: 
--     * Slot: id Description: 
--     * Slot: first_name Description: 
--     * Slot: last_name Description: 
--     * Slot: middle_initial Description: 
--     * Slot: orcid Description: 
--     * Slot: profile_image_url Description: 
--     * Slot: websites Description: 
-- # Class: "quantityValue" Description: "A quantity value with numeric value and optional unit"
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: has_value_unit Description: 
--     * Slot: has_unit Description: The human-readable unit name
--     * Slot: has_numeric_value Description: The numeric value of the quantity
--     * Slot: has_minimum_numeric_value Description: 
--     * Slot: has_maximum_numeric_value Description: 
--     * Slot: has_raw_value Description: 
-- # Class: "geolocationValue" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: has_raw_value Description: 
--     * Slot: latitude Description: 
--     * Slot: longitude Description: 
--     * Slot: type Description: 
--     * Slot: was_generated_by Description: 
-- # Class: "conditioningValue" Description: ""
--     * Slot: id Description: 
--     * Slot: source_material Description: 
--     * Slot: type Description: 
--     * Slot: instrument Description: 
--     * Slot: gas Description: 
--     * Slot: pressure Description: 
--     * Slot: has_raw_value Description: 
-- # Class: "latLongValue" Description: ""
--     * Slot: id Description: 
--     * Slot: description Description: 
--     * Slot: has_raw_value Description: 
--     * Slot: latitude Description: 
--     * Slot: longitude Description: 
-- # Class: "magBin" Description: ""
--     * Slot: id Description: 
--     * Slot: workflow_id Description: 
--     * Slot: bin_name Description: 
--     * Slot: bin_quality Description: 
--     * Slot: completeness Description: 
--     * Slot: contamination Description: 
--     * Slot: gene_count Description: 
--     * Slot: gtdbtk_class Description: 
--     * Slot: gtdbtk_domain Description: 
--     * Slot: gtdbtk_family Description: 
--     * Slot: gtdbtk_genus Description: 
--     * Slot: gtdbtk_order Description: 
--     * Slot: gtdbtk_phylum Description: 
--     * Slot: gtdbtk_species Description: 
--     * Slot: members_id Description: 
--     * Slot: num_16s Description: 
--     * Slot: num_23s Description: 
--     * Slot: num_5s Description: 
--     * Slot: num_trna Description: 
--     * Slot: number_of_contig Description: 
--     * Slot: total_bases Description: 
-- # Class: "soil" Description: ""
--     * Slot: id Description: 
--     * Slot: annual_precpt_id Description: 
--     * Slot: annual_temp_id Description: 
--     * Slot: bulk_elect_conductivity_id Description: 
--     * Slot: density_id Description: 
--     * Slot: depth_id Description: 
--     * Slot: particle_class_id Description: 
--     * Slot: porosity_id Description: 
--     * Slot: pressure_id Description: 
--     * Slot: season_precpt_id Description: 
--     * Slot: season_temp_id Description: 
--     * Slot: size_frac_low_id Description: 
--     * Slot: size_frac_up_id Description: 
--     * Slot: slope_aspect_id Description: 
--     * Slot: slope_gradient_id Description: 
--     * Slot: soil_temperature_id Description: 
--     * Slot: soil_texture_id Description: 
--     * Slot: temp_id Description: 
--     * Slot: water_content_id Description: 
--     * Slot: wind_speed_id Description: 
--     * Slot: cur_land_use Description: 
--     * Slot: drainage_class Description: 
--     * Slot: fao_class Description: 
--     * Slot: neon_domain Description: 
--     * Slot: profile_position Description: 
--     * Slot: sediment_type Description: 
--     * Slot: soil_horizon Description: 
--     * Slot: tillage Description: 
--     * Slot: wind_direction Description: 
--     * Slot: agrochem_addition Description: 
--     * Slot: al_sat Description: 
--     * Slot: al_sat_meth Description: 
--     * Slot: biotic_regm Description: 
--     * Slot: climate_environment Description: 
--     * Slot: core_collector Description: 
--     * Slot: crop_rotation Description: 
--     * Slot: crop_rotation_schedule Description: 
--     * Slot: cur_vegetation Description: 
--     * Slot: cur_vegetation_meth Description: 
--     * Slot: filter_method Description: 
--     * Slot: fire Description: 
--     * Slot: flooding Description: 
--     * Slot: heavy_metals Description: 
--     * Slot: heavy_metals_meth Description: 
--     * Slot: horizon_meth Description: 
--     * Slot: infiltration_1 Description: 
--     * Slot: infiltration_2 Description: 
--     * Slot: infiltration_notes Description: 
--     * Slot: link_class_info Description: 
--     * Slot: link_climate_info Description: 
--     * Slot: local_class Description: 
--     * Slot: local_class_meth Description: 
--     * Slot: perturbation Description: 
--     * Slot: previous_land_use Description: 
--     * Slot: previous_land_use_meth Description: 
--     * Slot: site_definition Description: 
--     * Slot: soil_type Description: 
--     * Slot: soil_type_meth Description: 
--     * Slot: texture_meth Description: 
--     * Slot: water_content_meth Description: 
--     * Slot: weather Description: 
-- # Class: "siteMetadata" Description: ""
--     * Slot: id Description: 
--     * Slot: nasa_mean_annual_temp_c_id Description: 
--     * Slot: nasa_mean_annual_precip_mm_id Description: 
--     * Slot: nasa_max_annual_temp_c_id Description: 
--     * Slot: nasa_min_annual_temp_c_id Description: 
--     * Slot: nasa_mean_wind_speed_ms_id Description: 
--     * Slot: nasa_mean_relative_humidity_pct_id Description: 
--     * Slot: nasa_frost_days_per_year_id Description: 
--     * Slot: nasa_mean_dew_point_c_id Description: 
--     * Slot: nasa_mean_vapor_pressure_kpa_id Description: 
--     * Slot: nasa_mean_surface_pressure_kpa_id Description: 
--     * Slot: nasa_mean_shortwave_radiation_wm2_id Description: 
--     * Slot: nasa_mean_longwave_radiation_wm2_id Description: 
--     * Slot: created_at Description: 
--     * Slot: updated_at Description: 
--     * Slot: cache_key Description: 
--     * Slot: latitude Description: 
--     * Slot: longitude Description: 
--     * Slot: provider Description: 
--     * Slot: enriched_at Description: 
-- # Class: "sampling_activity_site_metadata_link" Description: ""
--     * Slot: id Description: 
--     * Slot: sampling_activity_id Description: 
--     * Slot: site_metadata_id Description: 
-- # Class: "BulkDensityMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: id Description: 
-- # Class: "ElementalAnalysisMethod" Description: ""
--     * Slot: id Description: 
-- # Class: "EnzymeActivityMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: incubation_temp_c Description: 
--     * Slot: incubation_time Description: 
--     * Slot: wavelength Description: 
--     * Slot: method Description: 
-- # Class: "FTICR_AcquisitionMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: injection Description: 
--     * Slot: ionization Description: 
--     * Slot: polarity Description: 
--     * Slot: iat Description: 
--     * Slot: fid Description: 
--     * Slot: mass_range Description: 
-- # Class: "GravimetricWaterContentMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
-- # Class: "HydraulicPropertiesMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: fitting_model Description: 
-- # Class: "KuoMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: method Description: 
--     * Slot: id Description: 
--     * Slot: detection_limit Description: 
--     * Slot: wavelength Description: 
-- # Class: "LCMS_MetabolomicsMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: injection Description: 
--     * Slot: polarity Description: 
--     * Slot: column Description: 
--     * Slot: mode Description: 
--     * Slot: method_duration Description: 
--     * Slot: runtime Description: 
--     * Slot: resolution Description: 
--     * Slot: scan_range Description: 
--     * Slot: dd_ms2_resolution Description: 
--     * Slot: loop_count Description: 
--     * Slot: isolation_window Description: 
-- # Class: "MicrobialBiomassMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: detector Description: 
--     * Slot: mode Description: 
--     * Slot: injection_volume Description: 
--     * Slot: sample_volume Description: 
--     * Slot: number_of_injections Description: 
--     * Slot: check_standard_spacing Description: 
-- # Class: "PH_Method" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: calibration Description: 
-- # Class: "RespirationMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: id Description: 
--     * Slot: respiration_analysis_type Description: 
--     * Slot: sample_volume_id Description: 
--     * Slot: scale_id Description: 
--     * Slot: duration_id Description: 
--     * Slot: sampling_time_id Description: 
--     * Slot: bottle_vol_id Description: 
-- # Class: "TOC_TN_Method" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: column Description: 
--     * Slot: mode Description: 
--     * Slot: detector Description: 
--     * Slot: injection_volume Description: 
--     * Slot: sample_volume Description: 
--     * Slot: number_of_injections Description: 
--     * Slot: check_standard_spacing Description: 
-- # Class: "TextureMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: method Description: 
--     * Slot: id Description: 
-- # Class: "XrayComputedTomographyMethod" Description: ""
--     * Slot: analytic Description: 
--     * Slot: location Description: 
--     * Slot: id Description: 
--     * Slot: x_ray_power Description: 
--     * Slot: cu_filter Description: 
--     * Slot: total_projections_collected Description: 
--     * Slot: rotation Description: 
--     * Slot: frames_recording_per_projection Description: 
--     * Slot: exposure_time_per_frame Description: 
--     * Slot: image_voxel_size_is Description: 
-- # Class: "BulkDensityProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: bulk_density_id Description: 
--     * Slot: flag Description: 
-- # Class: "ElementalAnalysisProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: total_carbon_id Description: 
--     * Slot: total_nitrogen_id Description: 
--     * Slot: total_kjeldahl_nitrogen_id Description: 
--     * Slot: total_sulfur_id Description: 
--     * Slot: flag_total_carbon Description: 
--     * Slot: flag_total_nitrogen Description: 
--     * Slot: flag_tkn Description: 
--     * Slot: flag_total_sulfur Description: 
-- # Class: "EnzymeProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: beta_glucosidase_ug_pnp_per_g_per_h_id Description: 
--     * Slot: flag Description: 
-- # Class: "FTICRProduct" Description: ""
--     * Slot: id Description: 
--     * Slot: measure_type Description: 
--     * Slot: rep Description: 
--     * Slot: aq Description: 
--     * Slot: h_c_average Description: 
--     * Slot: o_c_average Description: 
--     * Slot: c_average Description: 
--     * Slot: percent_mz_assigned_id Description: 
--     * Slot: rms_id Description: 
--     * Slot: dbe_average Description: 
--     * Slot: low_mass_accuracy_flag Description: 
--     * Slot: low_mz_assignment_flag Description: 
-- # Class: "GWCMoistureProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: gwc_percent_id Description: 
--     * Slot: flag Description: 
-- # Class: "IonsAnalysisProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: sulfate_id Description: 
--     * Slot: boron_id Description: 
--     * Slot: zinc_id Description: 
--     * Slot: manganate_id Description: 
--     * Slot: copper_id Description: 
--     * Slot: iron_id Description: 
--     * Slot: calcium_id Description: 
--     * Slot: magnesium_id Description: 
--     * Slot: sodium_id Description: 
--     * Slot: potassium_id Description: 
--     * Slot: total_bases_id Description: 
--     * Slot: cation_exchange_capacity_id Description: 
--     * Slot: flag_sulfate Description: 
--     * Slot: flag_boron Description: 
--     * Slot: flag_zinc Description: 
--     * Slot: flag_manganate Description: 
--     * Slot: flag_copper Description: 
--     * Slot: flag_iron Description: 
--     * Slot: flag_calcium Description: 
--     * Slot: flag_magnesium Description: 
--     * Slot: flag_sodium Description: 
--     * Slot: flag_potassium Description: 
--     * Slot: flag_total_bases Description: 
--     * Slot: flag_cec Description: 
-- # Class: "MAOMProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: rep Description: 
--     * Slot: id Description: 
--     * Slot: total_organic_carbon_id Description: 
--     * Slot: total_organic_carbon_avg Description: 
--     * Slot: total_nitrogen_id Description: 
--     * Slot: total_nitrogen_avg Description: 
--     * Slot: flag_toc Description: 
--     * Slot: flag_tn Description: 
--     * Slot: flag_toc_avg Description: 
--     * Slot: flag_tn_avg Description: 
-- # Class: "MetaGenomicsProduct" Description: ""
--     * Slot: id Description: 
--     * Slot: input_to_step Description: 
--     * Slot: output_to_step Description: 
-- # Class: "MicrobialBiomassProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: rep Description: 
--     * Slot: id Description: 
--     * Slot: mbc_id Description: 
--     * Slot: mbc_avg Description: 
--     * Slot: mbn_id Description: 
--     * Slot: mbn_avg Description: 
--     * Slot: flag_mbc Description: 
--     * Slot: flag_mbn Description: 
--     * Slot: flag_mbc_avg Description: 
--     * Slot: flag_mbn_avg Description: 
-- # Class: "NitrogenAnalysisProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: rep Description: 
--     * Slot: id Description: 
--     * Slot: no3_n_id Description: 
--     * Slot: no3_n_avg Description: 
--     * Slot: nh4_n_id Description: 
--     * Slot: nh4_n_avg Description: 
--     * Slot: flag_no3n Description: 
--     * Slot: flag_nh4n Description: 
--     * Slot: flag_no3n_avg Description: 
--     * Slot: flag_nh4n_avg Description: 
-- # Class: "PhosphorusAnalysisProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: rep Description: 
--     * Slot: id Description: 
--     * Slot: extraction_method Description: 
--     * Slot: phosphorus_id Description: 
--     * Slot: phosphorus_avg Description: 
--     * Slot: flag Description: 
--     * Slot: flag_avg Description: 
-- # Class: "RespirationProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: respiration_rate_per_day_id Description: 
--     * Slot: flag Description: 
-- # Class: "TextureProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: sand_pct_id Description: 
--     * Slot: silt_pct_id Description: 
--     * Slot: clay_pct_id Description: 
--     * Slot: flag Description: 
-- # Class: "TomographyProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: roi_volume_voxel Description: 
--     * Slot: voxel_size Description: 
--     * Slot: connected_pores Description: 
--     * Slot: pore_diameter_min Description: 
--     * Slot: pore_diameter_max Description: 
--     * Slot: pore_diameter_mean Description: 
--     * Slot: pore_diameter_median Description: 
--     * Slot: pore_diameter_variance Description: 
--     * Slot: pore_volume_mean Description: 
--     * Slot: total_pore_volume Description: 
--     * Slot: permeability_x Description: 
--     * Slot: flow_rate_x Description: 
--     * Slot: tortuosity_x Description: 
--     * Slot: permeability_y Description: 
--     * Slot: flow_rate_y Description: 
--     * Slot: tortuosity_y Description: 
--     * Slot: permeability_z Description: 
--     * Slot: flow_rate_z Description: 
--     * Slot: tortuosity_z Description: 
--     * Slot: flag_xct Description: 
-- # Class: "WEOMProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: rep Description: 
--     * Slot: id Description: 
--     * Slot: total_organic_carbon_id Description: 
--     * Slot: total_organic_carbon_avg Description: 
--     * Slot: total_nitrogen_id Description: 
--     * Slot: total_nitrogen_avg Description: 
--     * Slot: flag_toc Description: 
--     * Slot: flag_tn Description: 
--     * Slot: flag_toc_avg Description: 
--     * Slot: flag_tn_avg Description: 
-- # Class: "pHProduct" Description: ""
--     * Slot: measure_type Description: 
--     * Slot: id Description: 
--     * Slot: ph Description: 
--     * Slot: flag Description: 
-- # Class: "changelog" Description: ""
--     * Slot: version Description: 
--     * Slot: changelog Description: 

CREATE TABLE study (
	id UUID NOT NULL, 
	participant_name TEXT NOT NULL, 
	principal_investigator TEXT, 
	collaborating_institution TEXT, 
	project_status VARCHAR(9), 
	project_start DATETIME, 
	project_end DATETIME, 
	proposal_title TEXT, 
	proposal_abstract TEXT, 
	project_id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "sampleBase" (
	id UUID NOT NULL, 
	sample_name TEXT, 
	proposal_id INTEGER, 
	sampling_set TEXT, 
	sample_base_type VARCHAR(16) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "alternativeIdentifier" (
	id UUID NOT NULL, 
	alternate_id TEXT NOT NULL, 
	alternate_identifier_type VARCHAR(17) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE ecoregion (
	domain_id INTEGER NOT NULL, 
	domain_name TEXT NOT NULL, 
	PRIMARY KEY (domain_id)
);
CREATE TABLE "functionalAnnotationIdentifier" (
	id UUID NOT NULL, 
	functional_identifier TEXT NOT NULL, 
	"database" VARCHAR(4) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE instrument (
	id UUID NOT NULL, 
	name TEXT NOT NULL, 
	alternative_names TEXT, 
	vendor VARCHAR(21), 
	model VARCHAR(24), 
	instrument_parameters TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "metaboliteQuantification" (
	id UUID NOT NULL, 
	description TEXT, 
	alternative_identifiers TEXT, 
	highest_similarity_score INTEGER, 
	metabolite_quantified TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ontologyClass" (
	id UUID NOT NULL, 
	description TEXT, 
	alternative_identifiers TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "peptideQuantification" (
	id UUID NOT NULL, 
	description TEXT, 
	all_proteins TEXT, 
	best_protein TEXT, 
	min_q_value NUMERIC, 
	peptide_sequence TEXT, 
	peptide_spectral_count INTEGER, 
	peptide_sum_masic_abundance NUMERIC, 
	PRIMARY KEY (id)
);
CREATE TABLE "zipDownload" (
	id UUID NOT NULL, 
	time DATETIME NOT NULL, 
	user TEXT NOT NULL, 
	files INTEGER NOT NULL, 
	packages TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "sampleProcessing" (
	id UUID NOT NULL, 
	analysis_type VARCHAR(32), 
	method_name VARCHAR(4), 
	processing_steps TEXT NOT NULL, 
	url TEXT, 
	version TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "timestampValue" (
	id UUID NOT NULL, 
	description TEXT, 
	has_raw_value TEXT, 
	type TEXT, 
	was_generated_by TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "textValue" (
	id UUID NOT NULL, 
	description TEXT, 
	language TEXT, 
	has_raw_value TEXT, 
	type TEXT, 
	was_generated_by TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "softwareControlledTermValue" (
	id UUID NOT NULL, 
	description TEXT, 
	name TEXT, 
	version TEXT, 
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "controlledTermValue" (
	id UUID NOT NULL, 
	description TEXT, 
	has_raw_value TEXT, 
	was_generated_by TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "personValue" (
	email TEXT, 
	id UUID NOT NULL, 
	first_name TEXT NOT NULL, 
	last_name TEXT NOT NULL, 
	middle_initial TEXT, 
	orcid TEXT, 
	profile_image_url TEXT, 
	websites TEXT, 
	PRIMARY KEY (id), 
	UNIQUE (email)
);
CREATE TABLE "quantityValue" (
	id UUID NOT NULL, 
	description TEXT, 
	has_value_unit TEXT, 
	has_unit TEXT, 
	has_numeric_value FLOAT, 
	has_minimum_numeric_value NUMERIC, 
	has_maximum_numeric_value NUMERIC, 
	has_raw_value TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "geolocationValue" (
	id UUID NOT NULL, 
	description TEXT, 
	has_raw_value TEXT, 
	latitude NUMERIC, 
	longitude NUMERIC, 
	type TEXT, 
	was_generated_by TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "conditioningValue" (
	id UUID NOT NULL, 
	source_material TEXT, 
	type TEXT, 
	instrument TEXT, 
	gas TEXT, 
	pressure TEXT, 
	has_raw_value TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "latLongValue" (
	id UUID NOT NULL, 
	description TEXT, 
	has_raw_value TEXT, 
	latitude FLOAT NOT NULL, 
	longitude FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE changelog (
	version TEXT NOT NULL, 
	changelog TEXT NOT NULL, 
	PRIMARY KEY (version)
);
CREATE TABLE "samplingActivity" (
	id UUID NOT NULL, 
	study_id UUID NOT NULL, 
	type VARCHAR(5) NOT NULL, 
	sample_name TEXT NOT NULL, 
	lims_barcode TEXT, 
	alt_id UUID, 
	elev_id UUID, 
	lat_lon_id UUID, 
	growth_facil VARCHAR(22), 
	other_growth_facil TEXT, 
	other_storage_condt TEXT, 
	oxygen_relationship VARCHAR(17), 
	sample_store_temp VARCHAR(9), 
	samp_biotic_relationship VARCHAR(11), 
	storage_condt VARCHAR(11), 
	air_temp_regm TEXT, 
	chem_administration TEXT, 
	collection_date DATETIME, 
	collection_time DATETIME, 
	env_broad_scale_other TEXT, 
	env_local_scale_other TEXT, 
	env_medium_other TEXT, 
	experimental_factor TEXT, 
	experimental_factor_other TEXT, 
	extraction_method TEXT, 
	extreme_event DATETIME, 
	gaseous_environment TEXT, 
	geo_loc_name TEXT, 
	humidity_regm TEXT, 
	isotope_exposure TEXT, 
	light_regm TEXT, 
	link_addit_analys TEXT, 
	method_development TEXT, 
	microbial_biomass_c_meth TEXT, 
	microbial_biomass_meth TEXT, 
	microbial_biomass_n_meth TEXT, 
	misc_param TEXT, 
	neon_plot_id TEXT, 
	non_microb_biomass_method TEXT, 
	other_sample_store_temp TEXT, 
	other_treatment TEXT, 
	ph FLOAT, 
	ph_meth TEXT, 
	salinity FLOAT, 
	salinity_method TEXT, 
	sample_collected TEXT, 
	sample_collection_dev TEXT, 
	sample_collection_method TEXT, 
	sample_end_time DATETIME, 
	sample_processing TEXT, 
	sample_start_time DATETIME, 
	season_environment TEXT, 
	shipped_sample_size TEXT, 
	sieving TEXT, 
	start_date_inc DATETIME, 
	tot_nitro_cont_meth TEXT, 
	tot_org_c_meth TEXT, 
	watering_regm TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(study_id) REFERENCES study (id), 
	FOREIGN KEY(alt_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(elev_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(lat_lon_id) REFERENCES "geolocationValue" (id)
);
CREATE TABLE "processedSample" (
	id UUID NOT NULL, 
	processed_sample_type VARCHAR(11) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "sampleBase" (id)
);
CREATE TABLE "containerType" (
	id UUID NOT NULL, 
	description TEXT, 
	was_generated_by TEXT, 
	container_type VARCHAR(17), 
	container_size_id UUID, 
	PRIMARY KEY (id), 
	FOREIGN KEY(container_size_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE custodian (
	id UUID NOT NULL, 
	person_id UUID, 
	PRIMARY KEY (id), 
	FOREIGN KEY(person_id) REFERENCES "personValue" (id)
);
CREATE TABLE instrument_alt_id (
	id UUID NOT NULL, 
	instrument_alt_id_provider VARCHAR(5), 
	instrument_id UUID NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "alternativeIdentifier" (id), 
	FOREIGN KEY(instrument_id) REFERENCES instrument (id)
);
CREATE TABLE "labDevice" (
	id UUID NOT NULL, 
	description TEXT, 
	device_type VARCHAR(14), 
	activity_time_id UUID, 
	activity_speed_id UUID, 
	PRIMARY KEY (id), 
	FOREIGN KEY(activity_time_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(activity_speed_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "processingSampleLink" (
	id UUID NOT NULL, 
	sample_base_id UUID NOT NULL, 
	processing_id UUID NOT NULL, 
	step_number INTEGER NOT NULL, 
	role VARCHAR(13) NOT NULL, 
	version TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sample_base_id) REFERENCES "sampleBase" (id), 
	FOREIGN KEY(processing_id) REFERENCES "sampleProcessing" (id)
);
CREATE TABLE "siteMetadata" (
	id UUID NOT NULL, 
	nasa_mean_annual_temp_c_id UUID, 
	nasa_mean_annual_precip_mm_id UUID, 
	nasa_max_annual_temp_c_id UUID, 
	nasa_min_annual_temp_c_id UUID, 
	nasa_mean_wind_speed_ms_id UUID, 
	nasa_mean_relative_humidity_pct_id UUID, 
	nasa_frost_days_per_year_id UUID, 
	nasa_mean_dew_point_c_id UUID, 
	nasa_mean_vapor_pressure_kpa_id UUID, 
	nasa_mean_surface_pressure_kpa_id UUID, 
	nasa_mean_shortwave_radiation_wm2_id UUID, 
	nasa_mean_longwave_radiation_wm2_id UUID, 
	created_at TIMESTAMP NOT NULL, 
	updated_at TIMESTAMP NOT NULL, 
	cache_key TEXT NOT NULL, 
	latitude FLOAT NOT NULL, 
	longitude FLOAT NOT NULL, 
	provider TEXT NOT NULL, 
	enriched_at TIMESTAMP NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(nasa_mean_annual_temp_c_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_annual_precip_mm_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_max_annual_temp_c_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_min_annual_temp_c_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_wind_speed_ms_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_relative_humidity_pct_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_frost_days_per_year_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_dew_point_c_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_vapor_pressure_kpa_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_surface_pressure_kpa_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_shortwave_radiation_wm2_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nasa_mean_longwave_radiation_wm2_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE sample (
	id UUID NOT NULL, 
	sampling_activity_id UUID NOT NULL, 
	type VARCHAR(7), 
	guid_source TEXT, 
	other_guid_source TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "sampleBase" (id), 
	FOREIGN KEY(sampling_activity_id) REFERENCES "samplingActivity" (id)
);
CREATE TABLE "coreSection" (
	id UUID NOT NULL, 
	core_section VARCHAR(3) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedSample" (id)
);
CREATE TABLE replicate (
	id UUID NOT NULL, 
	rep INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedSample" (id)
);
CREATE TABLE "analysisActivity" (
	id UUID NOT NULL, 
	type VARCHAR(32), 
	analyte_id UUID, 
	name TEXT, 
	acquisition_time DATETIME NOT NULL, 
	instrument_id UUID, 
	protocol_url TEXT, 
	instrument_operator_id UUID, 
	version TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(analyte_id) REFERENCES "processedSample" (id), 
	FOREIGN KEY(instrument_id) REFERENCES instrument (id), 
	FOREIGN KEY(instrument_operator_id) REFERENCES "personValue" (id)
);
CREATE TABLE "instrumentCustodian" (
	id INTEGER NOT NULL, 
	instrument_id UUID NOT NULL, 
	custodian_id UUID NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(instrument_id) REFERENCES instrument (id), 
	FOREIGN KEY(custodian_id) REFERENCES custodian (id)
);
CREATE TABLE soil (
	id UUID NOT NULL, 
	annual_precpt_id UUID, 
	annual_temp_id UUID, 
	bulk_elect_conductivity_id UUID, 
	density_id UUID, 
	depth_id UUID, 
	particle_class_id UUID, 
	porosity_id UUID, 
	pressure_id UUID, 
	season_precpt_id UUID, 
	season_temp_id UUID, 
	size_frac_low_id UUID, 
	size_frac_up_id UUID, 
	slope_aspect_id UUID, 
	slope_gradient_id UUID, 
	soil_temperature_id UUID, 
	soil_texture_id UUID, 
	temp_id UUID, 
	water_content_id UUID, 
	wind_speed_id UUID, 
	cur_land_use VARCHAR(23), 
	drainage_class VARCHAR(19), 
	fao_class VARCHAR(11), 
	neon_domain VARCHAR(37), 
	profile_position VARCHAR(9), 
	sediment_type VARCHAR(11), 
	soil_horizon VARCHAR(10), 
	tillage VARCHAR(13), 
	wind_direction VARCHAR(10), 
	agrochem_addition TEXT, 
	al_sat FLOAT, 
	al_sat_meth TEXT, 
	biotic_regm TEXT, 
	climate_environment TEXT, 
	core_collector TEXT, 
	crop_rotation BOOLEAN, 
	crop_rotation_schedule TEXT, 
	cur_vegetation TEXT, 
	cur_vegetation_meth TEXT, 
	filter_method TEXT, 
	fire DATETIME, 
	flooding DATETIME, 
	heavy_metals TEXT, 
	heavy_metals_meth TEXT, 
	horizon_meth TEXT, 
	infiltration_1 TIME, 
	infiltration_2 TIME, 
	infiltration_notes TEXT, 
	link_class_info TEXT, 
	link_climate_info TEXT, 
	local_class TEXT, 
	local_class_meth TEXT, 
	perturbation TEXT, 
	previous_land_use TEXT, 
	previous_land_use_meth TEXT, 
	site_definition TEXT, 
	soil_type TEXT, 
	soil_type_meth TEXT, 
	texture_meth TEXT, 
	water_content_meth TEXT, 
	weather TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "samplingActivity" (id), 
	FOREIGN KEY(annual_precpt_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(annual_temp_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(bulk_elect_conductivity_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(density_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(depth_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(particle_class_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(porosity_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(pressure_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(season_precpt_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(season_temp_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(size_frac_low_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(size_frac_up_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(slope_aspect_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(slope_gradient_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(soil_temperature_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(soil_texture_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(temp_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(water_content_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(wind_speed_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE sampling_activity_site_metadata_link (
	id INTEGER NOT NULL, 
	sampling_activity_id UUID NOT NULL, 
	site_metadata_id UUID NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(sampling_activity_id) REFERENCES "samplingActivity" (id), 
	FOREIGN KEY(site_metadata_id) REFERENCES "siteMetadata" (id)
);
CREATE TABLE soil_sample (
	id UUID NOT NULL, 
	soil_type VARCHAR(13) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES sample (id)
);
CREATE TABLE aerosol_sample (
	id UUID NOT NULL, 
	aerosol_type VARCHAR(12) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES sample (id)
);
CREATE TABLE "instrumentData" (
	id UUID NOT NULL, 
	analysis_activity_id UUID, 
	description TEXT NOT NULL, 
	alternative_identifiers TEXT, 
	compression_type TEXT, 
	file_size_bytes INTEGER, 
	md5_checksum TEXT, 
	name TEXT NOT NULL, 
	type TEXT, 
	url TEXT, 
	was_generated_by TEXT, 
	file_type VARCHAR(49), 
	version TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(analysis_activity_id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "BulkDensityMethod" (
	analytic TEXT NOT NULL, 
	id UUID NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "ElementalAnalysisMethod" (
	id UUID NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "EnzymeActivityMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	incubation_temp_c FLOAT, 
	incubation_time TEXT, 
	wavelength FLOAT, 
	method TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "FTICR_AcquisitionMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	injection TEXT NOT NULL, 
	ionization VARCHAR(5) NOT NULL, 
	polarity TEXT NOT NULL, 
	iat FLOAT, 
	fid FLOAT, 
	mass_range FLOAT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "GravimetricWaterContentMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "HydraulicPropertiesMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	fitting_model TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "KuoMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	method TEXT NOT NULL, 
	id UUID NOT NULL, 
	detection_limit TEXT NOT NULL, 
	wavelength TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "LCMS_MetabolomicsMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	injection TEXT NOT NULL, 
	polarity TEXT NOT NULL, 
	"column" TEXT NOT NULL, 
	mode TEXT NOT NULL, 
	method_duration TEXT NOT NULL, 
	runtime TEXT NOT NULL, 
	resolution FLOAT NOT NULL, 
	scan_range TEXT NOT NULL, 
	dd_ms2_resolution FLOAT NOT NULL, 
	loop_count TEXT NOT NULL, 
	isolation_window TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "MicrobialBiomassMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	detector TEXT NOT NULL, 
	mode TEXT, 
	injection_volume TEXT NOT NULL, 
	sample_volume TEXT NOT NULL, 
	number_of_injections FLOAT NOT NULL, 
	check_standard_spacing TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "PH_Method" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	calibration TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "RespirationMethod" (
	analytic TEXT NOT NULL, 
	id UUID NOT NULL, 
	respiration_analysis_type TEXT NOT NULL, 
	sample_volume_id UUID, 
	scale_id UUID, 
	duration_id UUID, 
	sampling_time_id UUID, 
	bottle_vol_id UUID, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id), 
	FOREIGN KEY(sample_volume_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(scale_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(duration_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(sampling_time_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(bottle_vol_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "TOC_TN_Method" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	"column" TEXT, 
	mode TEXT, 
	detector TEXT NOT NULL, 
	injection_volume TEXT NOT NULL, 
	sample_volume TEXT NOT NULL, 
	number_of_injections FLOAT NOT NULL, 
	check_standard_spacing TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "TextureMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	method TEXT NOT NULL, 
	id UUID NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "XrayComputedTomographyMethod" (
	analytic TEXT NOT NULL, 
	location TEXT NOT NULL, 
	id UUID NOT NULL, 
	x_ray_power TEXT NOT NULL, 
	cu_filter TEXT NOT NULL, 
	total_projections_collected FLOAT NOT NULL, 
	rotation TEXT NOT NULL, 
	frames_recording_per_projection FLOAT NOT NULL, 
	exposure_time_per_frame TEXT NOT NULL, 
	image_voxel_size_is TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "analysisActivity" (id)
);
CREATE TABLE "workflowExecutionActivity" (
	id UUID NOT NULL, 
	raw_data_id UUID NOT NULL, 
	description TEXT, 
	ended_at_time DATETIME, 
	git_url TEXT NOT NULL, 
	name TEXT, 
	started_at_time DATETIME NOT NULL, 
	type TEXT NOT NULL, 
	used_id UUID, 
	execution_resource VARCHAR(6), 
	workflow_steps TEXT, 
	version TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(raw_data_id) REFERENCES "instrumentData" (id), 
	FOREIGN KEY(used_id) REFERENCES "softwareControlledTermValue" (id)
);
CREATE TABLE "processedData" (
	id UUID NOT NULL, 
	type VARCHAR(26) NOT NULL, 
	name TEXT NOT NULL, 
	proposal_id NUMERIC, 
	sampling_set NUMERIC, 
	core_section TEXT, 
	sample_name TEXT, 
	s3_base_url TEXT, 
	s3_bucket TEXT, 
	s3_key TEXT NOT NULL, 
	filesize INTEGER, 
	md5checksum TEXT, 
	workflow_id UUID, 
	lims_barcode TEXT, 
	version TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(workflow_id) REFERENCES "workflowExecutionActivity" (id)
);
CREATE TABLE "workflowExecutionFunctionalAnnotation" (
	id INTEGER NOT NULL, 
	workflow_id UUID NOT NULL, 
	functional_annotation_id UUID NOT NULL, 
	count NUMERIC, 
	PRIMARY KEY (id), 
	FOREIGN KEY(workflow_id) REFERENCES "workflowExecutionActivity" (id), 
	FOREIGN KEY(functional_annotation_id) REFERENCES "functionalAnnotationIdentifier" (id)
);
CREATE TABLE "magBin" (
	id UUID NOT NULL, 
	workflow_id UUID, 
	bin_name TEXT NOT NULL, 
	bin_quality VARCHAR(2), 
	completeness NUMERIC, 
	contamination NUMERIC, 
	gene_count INTEGER, 
	gtdbtk_class TEXT, 
	gtdbtk_domain TEXT, 
	gtdbtk_family TEXT, 
	gtdbtk_genus TEXT, 
	gtdbtk_order TEXT, 
	gtdbtk_phylum TEXT, 
	gtdbtk_species TEXT, 
	members_id TEXT, 
	num_16s INTEGER, 
	num_23s INTEGER, 
	num_5s INTEGER, 
	num_trna INTEGER, 
	number_of_contig INTEGER, 
	total_bases INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(workflow_id) REFERENCES "workflowExecutionActivity" (id)
);
CREATE TABLE "BulkDensityProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	bulk_density_id UUID, 
	flag VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(bulk_density_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "ElementalAnalysisProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	total_carbon_id UUID, 
	total_nitrogen_id UUID, 
	total_kjeldahl_nitrogen_id UUID, 
	total_sulfur_id UUID, 
	flag_total_carbon VARCHAR(21), 
	flag_total_nitrogen VARCHAR(21), 
	flag_tkn VARCHAR(21), 
	flag_total_sulfur VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(total_carbon_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(total_nitrogen_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(total_kjeldahl_nitrogen_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(total_sulfur_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "EnzymeProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	beta_glucosidase_ug_pnp_per_g_per_h_id UUID, 
	flag VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(beta_glucosidase_ug_pnp_per_g_per_h_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "FTICRProduct" (
	id UUID NOT NULL, 
	measure_type VARCHAR(9), 
	rep NUMERIC, 
	aq NUMERIC, 
	h_c_average FLOAT, 
	o_c_average FLOAT, 
	c_average FLOAT, 
	percent_mz_assigned_id UUID, 
	rms_id UUID, 
	dbe_average FLOAT, 
	low_mass_accuracy_flag BOOLEAN, 
	low_mz_assignment_flag BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(percent_mz_assigned_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(rms_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "GWCMoistureProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	gwc_percent_id UUID, 
	flag VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(gwc_percent_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "IonsAnalysisProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	sulfate_id UUID, 
	boron_id UUID, 
	zinc_id UUID, 
	manganate_id UUID, 
	copper_id UUID, 
	iron_id UUID, 
	calcium_id UUID, 
	magnesium_id UUID, 
	sodium_id UUID, 
	potassium_id UUID, 
	total_bases_id UUID, 
	cation_exchange_capacity_id UUID, 
	flag_sulfate VARCHAR(21), 
	flag_boron VARCHAR(21), 
	flag_zinc VARCHAR(21), 
	flag_manganate VARCHAR(21), 
	flag_copper VARCHAR(21), 
	flag_iron VARCHAR(21), 
	flag_calcium VARCHAR(21), 
	flag_magnesium VARCHAR(21), 
	flag_sodium VARCHAR(21), 
	flag_potassium VARCHAR(21), 
	flag_total_bases VARCHAR(21), 
	flag_cec VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(sulfate_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(boron_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(zinc_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(manganate_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(copper_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(iron_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(calcium_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(magnesium_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(sodium_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(potassium_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(total_bases_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(cation_exchange_capacity_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "MAOMProduct" (
	measure_type VARCHAR(9), 
	rep NUMERIC, 
	id UUID NOT NULL, 
	total_organic_carbon_id UUID, 
	total_organic_carbon_avg FLOAT, 
	total_nitrogen_id UUID, 
	total_nitrogen_avg FLOAT, 
	flag_toc VARCHAR(21), 
	flag_tn VARCHAR(21), 
	flag_toc_avg VARCHAR(21), 
	flag_tn_avg VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(total_organic_carbon_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(total_nitrogen_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "MetaGenomicsProduct" (
	id UUID NOT NULL, 
	input_to_step VARCHAR(25), 
	output_to_step VARCHAR(25) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id)
);
CREATE TABLE "MicrobialBiomassProduct" (
	measure_type VARCHAR(9), 
	rep NUMERIC, 
	id UUID NOT NULL, 
	mbc_id UUID, 
	mbc_avg FLOAT, 
	mbn_id UUID, 
	mbn_avg FLOAT, 
	flag_mbc VARCHAR(21), 
	flag_mbn VARCHAR(21), 
	flag_mbc_avg VARCHAR(21), 
	flag_mbn_avg VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(mbc_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(mbn_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "NitrogenAnalysisProduct" (
	measure_type VARCHAR(9), 
	rep NUMERIC, 
	id UUID NOT NULL, 
	no3_n_id UUID, 
	no3_n_avg FLOAT, 
	nh4_n_id UUID, 
	nh4_n_avg FLOAT, 
	flag_no3n VARCHAR(21), 
	flag_nh4n VARCHAR(21), 
	flag_no3n_avg VARCHAR(21), 
	flag_nh4n_avg VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(no3_n_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(nh4_n_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "PhosphorusAnalysisProduct" (
	measure_type VARCHAR(9), 
	rep NUMERIC, 
	id UUID NOT NULL, 
	extraction_method TEXT, 
	phosphorus_id UUID, 
	phosphorus_avg FLOAT, 
	flag VARCHAR(21), 
	flag_avg VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(phosphorus_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "RespirationProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	respiration_rate_per_day_id UUID, 
	flag VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(respiration_rate_per_day_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "TextureProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	sand_pct_id UUID, 
	silt_pct_id UUID, 
	clay_pct_id UUID, 
	flag VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(sand_pct_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(silt_pct_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(clay_pct_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "TomographyProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	roi_volume_voxel FLOAT, 
	voxel_size FLOAT, 
	connected_pores FLOAT, 
	pore_diameter_min FLOAT, 
	pore_diameter_max FLOAT, 
	pore_diameter_mean FLOAT, 
	pore_diameter_median FLOAT, 
	pore_diameter_variance FLOAT, 
	pore_volume_mean FLOAT, 
	total_pore_volume FLOAT, 
	permeability_x FLOAT, 
	flow_rate_x FLOAT, 
	tortuosity_x FLOAT, 
	permeability_y FLOAT, 
	flow_rate_y FLOAT, 
	tortuosity_y FLOAT, 
	permeability_z FLOAT, 
	flow_rate_z FLOAT, 
	tortuosity_z FLOAT, 
	flag_xct TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id)
);
CREATE TABLE "WEOMProduct" (
	measure_type VARCHAR(9), 
	rep NUMERIC, 
	id UUID NOT NULL, 
	total_organic_carbon_id UUID, 
	total_organic_carbon_avg FLOAT, 
	total_nitrogen_id UUID, 
	total_nitrogen_avg FLOAT, 
	flag_toc VARCHAR(21), 
	flag_tn VARCHAR(21), 
	flag_toc_avg VARCHAR(21), 
	flag_tn_avg VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id), 
	FOREIGN KEY(total_organic_carbon_id) REFERENCES "quantityValue" (id), 
	FOREIGN KEY(total_nitrogen_id) REFERENCES "quantityValue" (id)
);
CREATE TABLE "pHProduct" (
	measure_type VARCHAR(9), 
	id UUID NOT NULL, 
	ph FLOAT, 
	flag VARCHAR(21), 
	PRIMARY KEY (id), 
	FOREIGN KEY(id) REFERENCES "processedData" (id)
);
