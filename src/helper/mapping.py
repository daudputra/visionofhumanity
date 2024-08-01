import csv
import aiofiles
import asyncio

class Mapping:
    def __init__(self, file_csv) -> None:
        self.file_csv = file_csv

    @staticmethod
    def convert_value(value):
        try:
            int_value = int(value)
            return int_value
        except ValueError:
            try:
                float_value = float(value)
                return round(float_value, 3)
            except ValueError:
                return value
            

    def na_row(row):
        return ['N/A' if value == '-1' else value for value in row]

    @staticmethod
    async def get_overall_score(row,index):
        while True:  
            try:
                row = ['N/A' if value == '-1' else value for value in row]
                
                overall_score = row[index]
                if overall_score == 'N/A':
                    return 'N/A'
                else:
                    return round(float(overall_score), 2)
                # break
            except IndexError:  
                await asyncio.sleep(1)

    @staticmethod
    async def gpi_dict_data(row):
        row = Mapping.na_row(row)
        overall_score = await Mapping.get_overall_score(row,4)

        data_dict = {
            "code": Mapping.convert_value(row[0]),
            "name": Mapping.convert_value(row[1]),
            "year": Mapping.convert_value(row[2]),
            "rank": Mapping.convert_value(row[3]),
            "overall_indicator": Mapping.convert_value(row[4]),
            "overall_score": overall_score,
            "perceived_criminality_in_society": Mapping.convert_value(row[6]),
            "security_officers_and_police": Mapping.convert_value(row[8]),
            "homicides": Mapping.convert_value(row[10]),
            "jailed_population": Mapping.convert_value(row[12]),
            "access_to_weapons": Mapping.convert_value(row[14]),
            "organised_conflict_internal": Mapping.convert_value(row[16]),
            "violent_demonstrations": Mapping.convert_value(row[18]),
            "violent_crime": Mapping.convert_value(row[20]),
            "political_instability": Mapping.convert_value(row[22]),
            "political_terror": Mapping.convert_value(row[24]),
            "weapons_imports": Mapping.convert_value(row[26]),
            "terrorist_activity": Mapping.convert_value(row[28]),
            "internal_conflicts_fought": Mapping.convert_value(row[30]),
            "deaths_from_conflict_internal": Mapping.convert_value(row[32]),
            "military_expenditure": Mapping.convert_value(row[34]),
            "armed_services_personnel": Mapping.convert_value(row[36]),
            "un_peacekeeping_funding": Mapping.convert_value(row[38]),
            "nuclear_and_heavy_weapons": Mapping.convert_value(row[40]),
            "weapons_exports": Mapping.convert_value(row[42]),
            "displaced_people": Mapping.convert_value(row[44]),
            "neighbouring_country_relations": Mapping.convert_value(row[46]),
            "deaths_from_conflict_external": Mapping.convert_value(row[48]),
            "external_conflicts_fought": Mapping.convert_value(row[50]),
            "militarisation": Mapping.convert_value(row[52]),
            "safety_and_security": Mapping.convert_value(row[54]),
            "domestic_international_conflict": Mapping.convert_value(row[56])
        }

        return data_dict
                


    
    @staticmethod
    async def gti_dict_data(row):
        row = Mapping.na_row(row)
        overall_score = await Mapping.get_overall_score(row, 4)

        data_dict = {
            "code": Mapping.convert_value(row[0]),
            "name": Mapping.convert_value(row[1]),
            "year": Mapping.convert_value(row[2]),
            "rank": Mapping.convert_value(row[3]),
            "overall_score": overall_score,
            "terrorism_index": Mapping.convert_value(row[4]),
            "incidents" : Mapping.convert_value(row[6]),
            "fatalities" : Mapping.convert_value(row[8]),
            "injuries" : Mapping.convert_value(row[10]),
            "hostages" : Mapping.convert_value(row[12]),
        }
        return data_dict
    
    @staticmethod
    async def etr_dict_data(row):

        row = Mapping.na_row(row)
        overall_score = await Mapping.get_overall_score(row, 4)

        data_dict = {
            "code": Mapping.convert_value(row[0]),
            "name": Mapping.convert_value(row[1]),
            "year": Mapping.convert_value(row[8]),
            "rank": Mapping.convert_value(row[2]),
            "overall_score": overall_score,
            "etr_score" : Mapping.convert_value(row[3]),
            "food_security" : Mapping.convert_value(row[4]),
            "natural_disasters" : Mapping.convert_value(row[5]),
            "population_growth(2020-2050)" : Mapping.convert_value(row[6]),
            "water_risk" : Mapping.convert_value(row[7]),   
        }

        return data_dict

    @staticmethod
    async def mpi_dict_data(row):

        row = Mapping.na_row(row)
        overall_score = await Mapping.get_overall_score(row, 3)
        
        data_dict = {
            "code": Mapping.convert_value(row[1]),
            "name": Mapping.convert_value(row[0]),
            "year": Mapping.convert_value(row[2]),
            "rank": Mapping.convert_value(row[5]),
            "overall_score": overall_score,
            "mexico_peace_index": Mapping.convert_value(row[3]),
            "homicide" : Mapping.convert_value(row[6]),
            "violent_crime" : Mapping.convert_value(row[10]),
            "weapons_crime" : Mapping.convert_value(row[14]),
            "fear_of_violence" : Mapping.convert_value(row[8]),
            "organized_crime" : Mapping.convert_value(row[12]),
        }

        return data_dict
    
    @staticmethod
    async def ppi_dict_data(row):

        row = Mapping.na_row(row)
        overall_score = await Mapping.get_overall_score(row, 4)

        data_dict = {
            "code": Mapping.convert_value(row[0]),
            "name": Mapping.convert_value(row[1]),
            "year": Mapping.convert_value(row[2]),
            "rank": Mapping.convert_value(row[3]),
            "overall_score" : overall_score,
            "ppi_overall_score" : Mapping.convert_value(row[4]),
            "acceptance_of_the_rights_of_others" : Mapping.convert_value(row[6]),
            "equitable_distribution_of_resources" : Mapping.convert_value(row[8]),
            "free_flow_of_information" : Mapping.convert_value(row[10]),
            "good_relations_with_neighbours" : Mapping.convert_value(row[12]),
            "high_levels_of_human_capital" : Mapping.convert_value(row[14]),
            "low_levels_of_corruption" : Mapping.convert_value(row[16]),
            "sound_business_environment" : Mapping.convert_value(row[18]),
            "well-functioning_government" : Mapping.convert_value(row[20]),
        }
        return data_dict


    @staticmethod
    async def uspi_dict_data(row):
        row = Mapping.na_row(row)
        overall_score = await Mapping.get_overall_score(row, 3)

        data_dict = {
            "code": Mapping.convert_value(row[0]),
            "name": Mapping.convert_value(row[1]),
            "year": Mapping.convert_value(row[2]),
            "rank": Mapping.convert_value(row[5]),
            "overall_score": overall_score,
            "overall": Mapping.convert_value(row[3]),
            "homicide" : Mapping.convert_value(row[6]),
            "violent_crimes" : Mapping.convert_value(row[10]),
            "incarceration" : Mapping.convert_value(row[8]),
            "police_employees" : Mapping.convert_value(row[12]),
            "small_arms" : Mapping.convert_value(row[14]),
        }
        return data_dict


    @staticmethod
    async def ukpi_dict_data(row):

        row = Mapping.na_row(row)
        overall_score = await Mapping.get_overall_score(row, 3)


        data_dict = {
            "code": Mapping.convert_value(row[1]),
            "name": Mapping.convert_value(row[0]),
            "year" :Mapping.convert_value(row[15]),
            "rank" : Mapping.convert_value(row[4]),
            "overall_score" : overall_score,
            "country": Mapping.convert_value(row[2]),
            "uk_peace_index" : Mapping.convert_value(row[3]),
            "homicide" : Mapping.convert_value(row[5]),
            "homicide_rank" : Mapping.convert_value(row[6]),
            "violent_crime" : Mapping.convert_value(row[11]),
            "violent_crime_rank" : Mapping.convert_value(row[12]),
            "weapons_crime" : Mapping.convert_value(row[13]),
            "weapons_crime_rank" : Mapping.convert_value(row[14]),
            "public_disorder" : Mapping.convert_value(row[9]),
            "public_disorder_rank" : Mapping.convert_value(row[10]),
            "police_officers" : Mapping.convert_value(row[7]),
            "police_officers_rank" : Mapping.convert_value(row[8]),
        }
        return data_dict


    async def read_csv(self, file_path):
        async with aiofiles.open(file_path, mode='r', newline='', encoding='utf-8' ,errors='ignore') as file:
            reader = csv.reader(await file.readlines())
            next(reader)

            data = []
            for row in reader:

                if 'GPI' in self.file_csv:
                    data_dict = await self.gpi_dict_data(row)
                    data.append(data_dict)
                elif 'GTI' in self.file_csv:
                    data_dict = await self.gti_dict_data(row)
                    data.append(data_dict)
                elif 'ETR' in self.file_csv:
                    data_dict = await self.etr_dict_data(row)
                    data.append(data_dict)
                elif 'MPI' in self.file_csv:
                    data_dict = await self.mpi_dict_data(row)
                    data.append(data_dict)
                elif 'PPI' in self.file_csv:
                    data_dict = await self.ppi_dict_data(row)
                    data.append(data_dict)
                elif 'USPI' in self.file_csv:
                    data_dict = await self.uspi_dict_data(row)
                    data.append(data_dict)
                elif 'UKPI' in self.file_csv or 'ukpi' in self.file_csv:
                    data_dict = await self.ukpi_dict_data(row)
                    data.append(data_dict)

            return data
