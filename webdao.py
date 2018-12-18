# -*- coding: utf-8 -*-
import sys
import re, string
import MySQLdb
import urllib2
import demjson
import json
import connectiondb as conn

reload(sys)
sys.setdefaultencoding('Cp1252')


def insertContact(first_name,last_name,email,message,upload_at):

    query = "INSERT INTO contact_us (first_name, last_name, email, message,upload_at) VALUES (%s,%s,%s,%s,%s) ;"
    data = (first_name,last_name,email,message,upload_at)
    conn.run_query(query,data)


def selectArtists():

    query = "SELECT artist_id, first_name, last_name, fan_page, youtube, country_id, city_id, music_type, description FROM artist;"
    data = ""
    cursor = conn.run_query(query,data)
    artist_id = []
    first_name = []
    last_name = []
    fan_page = []
    youtube = []
    country_id = []
    city_id = []
    music_type = []
    description = []
    artists = []
    for (ai, fn, ln, fp, you, ci, citi, mt, de) in cursor:
        artist_id.append(ai)
        first_name.append(fn)
        last_name.append(ln)
        fan_page.append(fp)
        youtube.append(you)
        country_id.append(ci)
        city_id.append(citi)
        music_type.append(mt)
        description.append(de)

    i = 0
    for a in artist_id:

        artists.append({'artist_id':str(artist_id[i]),'first_name':first_name[i],'last_name': last_name[i],'fan_page':fan_page[i],'youtube':youtube[i],'country_id':country_id[i],'city_id':city_id[i],'music_type':music_type[i],'description':description[i]})
        i = i + 1

    data = {'artists': artists}
    final = json.dumps(data,ensure_ascii=False).encode('utf8')
    return final


def selectWriters():

    query = "SELECT writer_id, first_name, last_name, fan_page, blog, country_id, city_id, description FROM writer;"
    data = ""
    cursor = conn.run_query(query,data)
    writer_id = []
    first_name = []
    last_name = []
    fan_page = []
    blog = []
    country_id = []
    city_id = []
    description = []
    writers = []
    for (ai, fn, ln, fp, blo, ci, citi, de) in cursor:
        writer_id.append(ai)
        first_name.append(fn)
        last_name.append(ln)
        fan_page.append(fp)
        blog.append(blo)
        country_id.append(ci)
        city_id.append(citi)
        description.append(de)

    i = 0
    for a in writer_id:

        writers.append({'writer_id':str(writer_id[i]),'first_name':first_name[i],'last_name': last_name[i],'fan_page':fan_page[i],'blog':blog[i],'country_id':country_id[i],'city_id':city_id[i],'description':description[i]})
        i = i + 1

    data = {'writers': writers}
    final = json.dumps(data,ensure_ascii=False).encode('utf8')
    return final

def selectRadios():

    query = "SELECT radio_id, name, web, country_id, city_id, description FROM radio;"
    data = ""
    cursor = conn.run_query(query,data)
    radio_id = []
    name = []
    web = []
    country_id = []
    city_id = []
    description = []
    radios = []
    for (ai, fn, ln, ci, citi, de) in cursor:
        radio_id.append(ai)
        name.append(fn)
        web.append(ln)
        country_id.append(ci)
        city_id.append(citi)
        description.append(de)

    i = 0
    for a in radio_id:

        radios.append({'radio_id':str(radio_id[i]),'name':name[i],'web': web[i],'country_id':country_id[i],'city_id':city_id[i],'description':description[i]})
        i = i + 1

    data = {'radios': radios}
    final = json.dumps(data,ensure_ascii=False).encode('utf8')
    return final


def insertSuscriptions(first_name,last_name,email,upload_at):

    query = "INSERT INTO suscription (first_name, last_name, email, upload_at) VALUES (%s,%s,%s,%s) ;"
    data = (first_name,last_name,email,upload_at)
    conn.run_query(query,data)