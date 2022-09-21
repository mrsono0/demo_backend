# import csv
# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings") 
# # 프로젝트-프로젝트와 같은 앱 이름의 폴더 이름이다. 임포트 전에 적어야 한다.

# django.setup()

# from emhospital.models import EmHospital

# with open('./24병원.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         EmHospital.objects.create(
#             HosGoo = row[0],
#             HosDong = row[1],
#             HosName = row[2],
#             AlwaysTime = int(row[3]),
#             HosAddress = row[4],
#             HosSNA = row[5],
#             Latitude = float(row[6]),
#             Longitude = float(row[7]),
#         )
#         print(row)
