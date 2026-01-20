# Dictionaries 
anime_name={"Nnum_1":"One Piece is the number one aniem in the world.",
            "Num_2":"Naruto is the number two anime in the world.",
            "Num_3456":["Bleach","MHA","Black Clover","Demon Slayer"]
}

print(anime_name["Num_2"])

print(anime_name["Num_3456"][2])

anime_name["Num_3456"]=["ReZero","Haikyuu","Promised Never Land"]

print(anime_name["Num_3456"])



anime_watched={
    "One_Piece":{
    "Charecters":["Zoro","Luffy","Name","Robin"],
    "num_times_watched":1,
    },
    "Haikyuu":{
    "Charecters":["Hinata","Kageyama","Oikawa","Miya Twins"],
    "Num_times_wateched":100
    }
}

print(anime_watched["Haikyuu"]["Charecters"][2])