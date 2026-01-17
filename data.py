# data.py

curriculum_data = {
    "Form 1 (KSSM)": {
        "Bahasa Melayu": ["Pengenalan Komunikasi", "Mendengar dan Bertutur", "Membaca Bahan Sastera", "Membaca Bahan Bukan Sastera", "Menulis Karangan", "Tatabahasa", "Kesantunan Bahasa", "Puisi Tradisional", "Puisi Moden", "Prosa Tradisional", "Prosa Moden", "Drama"],
        "English Language": ["Let’s Get Started", "Health Is Wealth", "Time Out", "What’s the Buzz?", "Learning Is Fun", "The Game On", "Let’s Celebrate", "Adventure", "Science and Technology", "People and Culture"],
        "Mathematics": ["Rational Numbers", "Factors and Multiples", "Squares, Square Roots, Cubes and Cube Roots", "Ratios", "Algebraic Expressions", "Linear Equations", "Linear Inequalities", "Lines and Angles", "Basic Polygons", "Perimeter and Area", "Volume of Solid Shapes", "Data Handling"],
        "Science": ["Introduction to Science", "Cell as the Basic Unit of Life", "Matter", "The Periodic Table", "Air", "Light and Optics", "Heat", "Electricity and Magnetism", "Earth", "Nutrition", "The Environment"],
        "Sejarah": ["Pengenalan Ilmu Sejarah", "Zaman Prasejarah", "Tamadun Awal Dunia", "Tamadun Awal Asia Tenggara", "Kemunculan Kerajaan Alam Melayu", "Kegemilangan Kesultanan Melayu Melaka", "Warisan Kesultanan Melayu Melaka"],
        "Geography": ["Pengenalan Geografi", "Arah", "Peta Lakar", "Bumi", "Cuaca dan Iklim di Malaysia", "Bentuk Muka Bumi", "Saliran", "Penduduk Malaysia"],
        "RBT": ["Pengenalan Reka Bentuk dan Teknologi", "Proses Reka Bentuk", "Reka Bentuk Mekanikal", "Reka Bentuk Elektrik", "Reka Bentuk Elektronik", "Reka Bentuk Akuaponik"],
        "Islamic/Moral": ["Islamic: Al-Quran Sumber Ilmu", "Islamic: Konsep Akidah", "Islamic: Ibadah", "Moral: Nilai Kehidupan", "Moral: Kejujuran"]
    },
    "Form 2 (KSSM)": {
        "Bahasa Melayu": ["Pengenalan Kemahiran Bahasa", "Mendengar dan Bertutur", "Membaca Bahan Sastera", "Tatabahasa", "Drama"],
        "English Language": ["It’s All About Me", "Free Time", "Wild Weather", "Be Healthy", "Go Green"],
        "Mathematics": ["Number Bases", "Fractions & Decimals", "Coordinate Geometry", "Pythagoras’ Theorem", "Circles"],
        "Science": ["Scientific Methodology", "Cell Structure", "Nutrition", "Blood Circulatory System", "Biodiversity", "Ecosystems"],
        "Sejarah": ["Warisan Negara Bangsa", "Kesultanan Melayu Melaka", "Kegiatan Ekonomi", "Kejatuhan Melaka"],
        "Geography": ["Skala dan Jarak", "Peta Topografi", "Cuaca dan Iklim", "Telekomunikasi"],
        "RBT": ["Penyelesaian Masalah Inventif", "Aplikasi Teknologi", "Reka Bentuk Elektrik"]
    },
    "Form 3 (KSSM)": {
        "Bahasa Melayu": ["Kemahiran Berbahasa", "Karangan Berformat", "Puisi Moden", "Prosa Tradisional"],
        "English Language": ["It’s Personal", "Health Matters", "Ready, Set, Go!", "Our Environment"],
        "Mathematics": ["Indices", "Standard Form", "Financial Management", "Trigonometry", "Loci", "Statistics"],
        "Science": ["Scientific Skills", "Respiration", "Transportation", "Acids, Bases and Salts", "Genetics", "Space"],
        "Sejarah": ["Pendudukan Jepun", "Ancaman Komunis", "Usaha Kemerdekaan", "Pembentukan Malaysia"],
        "Geography": ["Tumbuh-tumbuhan Semula Jadi", "Sumber Mineral", "Kegiatan Ekonomi", "Pembangunan Mampan"],
        "RBT": ["Aplikasi Teknologi Mekanikal", "Reka Bentuk Akuaponik", "Penghasilan Produk"]
    },
    "Form 4 (KSSM)": {
        "Bahasa Melayu": ["Karangan Respons Terbuka", "Analisis Prosa", "Rumusan", "Pengucapan Awam"],
        "English Language": ["Let’s Chat", "Buy It!", "Mother Nature", "Social Issues"],
        "Sejarah": ["Warisan Negara Bangsa", "Konflik Dunia", "Era Peralihan Kuasa British", "Pilihan Raya", "Kemerdekaan"],
        "Mathematics": ["Functions and Graphs", "Number Bases", "Quadratic Equations", "Measures of Dispersion"],
        "Additional Mathematics": ["Functions", "Quadratic Functions", "Systems of Equations", "Differentiation", "Integration"],
        "Physics": ["Forces and Motion I & II", "Gravitation", "Heat", "Waves", "Light and Optics"],
        "Chemistry": ["Atomic Structure", "Chemical Bonding", "Stoichiometry", "Acids, Bases and Salts", "Rate of Reaction"],
        "Biology": ["Cell Biology", "Movement of Substances", "Metabolism and Enzymes", "Cell Division"],
        "Economics": ["Basic Economic Problems", "Demand & Supply", "Market Equilibrium"],
        "Accounting": ["Double Entry System", "Ledger Accounts", "Financial Statements"],
        "Computer Science": ["Problem Solving", "Algorithms", "Coding", "Computer Systems"]
    },
    "Form 5 (KSSM)": {
        "Bahasa Melayu": ["Karangan Berpandu", "Ulasan", "Tatabahasa", "Laras Bahasa"],
        "English Language": ["Real Life", "Consumerism", "Science and Innovation", "Global Citizenship"],
        "Sejarah": ["Kedaulatan Negara", "Perlembagaan Persekutuan", "Dasar Luar Malaysia", "Kecemerlangan Malaysia"],
        "Mathematics": ["Circles", "Mathematical Reasoning", "Probability", "Bearing", "Plans and Elevations"],
        "Additional Mathematics": ["Trigonometry", "Circular Measure", "Probability Distributions", "Matrices"],
        "Physics": ["Electromagnetism", "Electronics", "Nuclear Physics"],
        "Chemistry": ["Redox Reactions", "Carbon Compounds", "Thermochemistry", "Polymer Chemistry"],
        "Biology": ["Locomotion and Support", "Coordination and Response", "Reproduction", "Inheritance", "Ecosystem"],
        "Economics": ["National Income", "Money and Banking", "Inflation", "International Trade"],
        "Accounting": ["Control Accounts", "Manufacturing Accounts", "Cash Flow Statements"]
    },
    "Form 6 (STPM)": {
        "Pengajian Am": ["P1: Sistem Tadbir Urus", "P1: Perlembagaan", "P2: Analisis Data", "P3: Kerja Kursus"],
        "MUET": ["Listening Skills", "Speaking Skills", "Reading Skills", "Writing Skills"],
        "Mathematics (T)": ["P1: Functions & Matrices", "P2: Calculus", "P3: Vectors & Statistics"],
        "Physics": ["P1: Mechanics", "P2: Electricity & Magnetism", "P3: Quantum Physics"],
        "Chemistry": ["P1: Physical Chemistry", "P2: Inorganic Chemistry", "P3: Organic Chemistry"],
        "Biology": ["P1: Cell Structure", "P2: Physiology", "P3: Genetics & Ecology"],
        "Economics": ["P1: Microeconomics", "P2: Macroeconomics", "P3: Malaysian Economy"],
        "Business Studies": ["Business Environment", "Marketing", "Strategic Management"],
        "Accounting": ["Financial Accounting", "Costing", "Auditing"]
    }
}
