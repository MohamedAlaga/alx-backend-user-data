import csv

# Input database data as a multi-line string (can be replaced with a file read)
data = """
Id	userId	Name	age	weight	BMI	BMR	FFM	LBM	BFP	TBW	CaloricNeed	WaterIntake	IdealBodyWeight	DailyProtenNeedInGrams
6F98D438-438E-4675-3498-08DD3036A4F8	a4059c44-8a45-4200-bfa8-bd618696d3ea	inbody	22	95	28.68011	1816.5	62.62768	62.62768	34.07613	45.7182	2815	3.135	72.30315	133
6613C126-BD75-4E04-5C53-08DD30376AD2	a4059c44-8a45-4200-bfa8-bd618696d3ea	string	22	98	28.02482	1877.75	65.37601	65.37601	33.28979	47.72449	2910	3.234	76.83071	137
"""
# Parse the input data into rows
lines = data.strip().split("\n")
reader = csv.DictReader(lines, delimiter='\t')
workouts = list(reader)

# Generate C# object list
cs_objects = "new List<Inbody>(){\n"
for workout in workouts:
    cs_objects += f"    new Inbody {{\n"
    cs_objects += f"        Id = Guid.Parse(\"{workout['Id']}\"),\n"
    cs_objects += f"        userId = \"{workout['userId']}\",\n"
    cs_objects += f"        Name = {workout['Name']},\n"
    cs_objects += f"        age = (float) {workout['age']},\n"
    cs_objects += f"        weight = (float) {workout['weight']},\n"
    cs_objects += f"        BMI = (float) {workout['BMI']},\n"
    cs_objects += f"        BMR = (float) {workout['BMR']},\n"
    cs_objects += f"        FFM = (float) {workout['FFM']},\n"
    cs_objects += f"        LBM = (float) {workout['LBM']},\n"
    cs_objects += f"        BFP = (float) {workout['BFP']},\n"
    cs_objects += f"        TBW = (float) {workout['TBW']},\n"
    cs_objects += f"        CaloricNeed = (float) {workout['CaloricNeed']},\n"
    cs_objects += f"        WaterIntake = (float) {workout['WaterIntake']},\n"
    cs_objects += f"        IdealBodyWeight = (float) {workout['IdealBodyWeight']},\n"
    cs_objects += f"        DailyProtenNeedInGrams = {workout['DailyProtenNeedInGrams']},\n"
    cs_objects += f"    }},\n"

cs_objects = cs_objects.rstrip(",\n") + "\n};"

# Output the generated C# objects
print(cs_objects)