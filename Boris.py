#задача здесь извлечь парамтетры и информацию только об одной лошади
import requests
response= requests.get("https://knowyourhorses.com/horses?search=Boris+the+Blue")
print(response)
#он не выдает не каких значений
# сейчас я поробую задать только одного бориса
# я не понял как задать переменную что бы он строго дал какието данные по Борису


