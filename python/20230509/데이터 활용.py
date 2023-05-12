data = [
    {
        "_id": "6459c9d0d350c58318887f41",
        "age": 26,
        "eyeColor": "blue",
        "name": "Marks Ryan",
        "gender": "male",
    },
    {
        "_id": "6459c9d09b36504f0d945206",
        "age": 24,
        "eyeColor": "green",
        "name": "Gracie Bruce",
        "gender": "female",
    },
    {
        "_id": "6459c9d0e13794007e6802ca",
        "age": 40,
        "eyeColor": "blue",
        "name": "Garrison Stein",
        "gender": "male",
    },
    {
        "_id": "6459c9d09d4efc3ea92f8b81",
        "age": 27,
        "eyeColor": "green",
        "name": "Keith Estrada",
        "gender": "male",
    },
    {
        "_id": "6459c9d0dd597f344128d194",
        "age": 29,
        "eyeColor": "green",
        "name": "Lamb Dorsey",
        "gender": "male",
    },
    {
        "_id": "6459c9d0c4bcc5d76abf78d0",
        "age": 31,
        "eyeColor": "brown",
        "name": "Short Bradford",
        "gender": "male",
    },
]

average_age = sum(map(lambda x: x["age"], data)) / len(data)
male = len(list(filter(lambda x: x["gender"] == "male", data)))
female = len(list(filter(lambda x: x["gender"] == "female", data)))

print(f"평균나이는 {average_age} 입니다.\n성비는 남성 {male} : 여성 {female} 입니다.")

gender = list(map(lambda x: x["gender"], data))
gender_count = [gender.count("male"), gender.count("female")]
print(f"평균나이는 {average_age} 입니다.\n성비는 남성 {gender_count[0]} : 여성 {gender_count[1]} 입니다.")

gender = [i["gender"] for i in data]
gender_count = [gender.count("male"), gender.count("female")]
print(f"평균나이는 {average_age} 입니다.\n성비는 남성 {gender_count[0]} : 여성 {gender_count[1]} 입니다.")
