
from supabase import create_client, Client
import os
from datetime import datetime

SUPABASE_URL = ""
SUPABASE_KEY = ""
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

print("supabase_client yüklendi")

def get_user_by_email(email: str):
    response = supabase.table("users").select("*").eq("email", email).execute()
    if response.data:
        return response.data[0]
    return None


def get_user_history(user_id):
    try:
        result = supabase.table("history").select("*").eq("id_users", user_id).execute()
        print("get_user_history sonucu:", result.data)
        return result.data
    except Exception as e:
        print("get_user_history hatası:", e)


def insert_history(user_id, response):
    try:
        data = {"id_users": user_id, "response": response}
        result = supabase.table("history").insert(data).execute()
        print("insert_history sonucu:", result.data)
        return result.data
    except Exception as e:
        print("insert_history hatası:", e)




