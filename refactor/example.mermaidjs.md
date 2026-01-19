flowchart TD
    subgraph Original["🌍 Original Sample"]
        SS_Orig[("SoilSample_Original<br/>Entity")]
    end
    
    subgraph Subsampling["✂️ Subsampling"]
        SubsampleAct[[SubsamplingActivity]]
        SS_Sub[("SoilSample_Subsample<br/>Entity")]
        SS_Pheno[("SoilSample_ForPhenotyping<br/>Entity")]
    end
    
    subgraph Phenotyping["🔬 Phenotyping"]
        PhenoAct[[PhenotypingActivity]]
        PhenoData[("PhenotypingData<br/>Entity")]
    end
    
    subgraph Growing["🌱 Plant Growing"]
        GrowAct[[PlantGrowingActivity]]
        Plant[("GrownPlant<br/>Entity")]
        PostSoil[("PostGrowthSoil<br/>Entity")]
        Flowers[("FlowerSample<br/>Entity")]
    end
    
    subgraph FlowerAnalyses["🌸 Flower Analyses"]
        ColorAct[[FlowerColorAnalysis]]
        SizeAct[[FlowerSizeAnalysis]]
        PollenAct[[PollenAnalysis]]
        ColorData[("ColorAnalysisData")]
        SizeData[("SizeAnalysisData")]
        PollenData[("PollenAnalysisData")]
    end
    
    subgraph SoilAnalyses["🧪 Soil Analyses"]
        NutrientAct[[SoilNutrientAnalysis]]
        MicrobialAct[[SoilMicrobialAnalysis]]
        NutrientData[("NutrientAnalysisData")]
        MicrobialData[("MicrobialAnalysisData")]
    end
    
    %% Relationships
    SS_Orig -->|Used| SubsampleAct
    SubsampleAct -->|WasGeneratedBy| SS_Sub
    SubsampleAct -->|WasGeneratedBy| SS_Pheno
    SS_Sub -.->|WasDerivedFrom| SS_Orig
    SS_Pheno -.->|WasDerivedFrom| SS_Orig
    
    SS_Pheno -->|Used| PhenoAct
    PhenoAct -->|WasGeneratedBy| PhenoData
    
    SS_Sub -->|Used| GrowAct
    GrowAct -->|WasGeneratedBy| Plant
    GrowAct -->|WasGeneratedBy| PostSoil
    GrowAct -->|WasGeneratedBy| Flowers
    Plant -.->|WasDerivedFrom| SS_Sub
    PostSoil -.->|WasDerivedFrom| SS_Sub
    Flowers -.->|WasDerivedFrom| SS_Sub
    
    %% Flower analyses
    Flowers -->|Used| ColorAct
    Flowers -->|Used| SizeAct
    Flowers -->|Used| PollenAct
    ColorAct -->|WasGeneratedBy| ColorData
    SizeAct -->|WasGeneratedBy| SizeData
    PollenAct -->|WasGeneratedBy| PollenData
    
    %% Soil analyses
    PostSoil -->|Used| NutrientAct
    PostSoil -->|Used| MicrobialAct
    NutrientAct -->|WasGeneratedBy| NutrientData
    MicrobialAct -->|WasGeneratedBy| MicrobialData
    
    %% Activity communication
    GrowAct -.->|WasInformedBy| PhenoAct

    style SS_Orig fill:#90EE90
    style Plant fill:#98FB98
    style Flowers fill:#FFB6C1
    style PostSoil fill:#DEB887
    style PhenoData fill:#87CEEB
    style ColorData fill:#87CEEB
    style SizeData fill:#87CEEB
    style PollenData fill:#87CEEB
    style NutrientData fill:#87CEEB
    style MicrobialData fill:#87CEEB