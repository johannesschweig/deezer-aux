import requests
import json
import sys

with open('files.txt') as f:
    for query in f:
      # cut of \n
      query = query[:-1].lower()
      # replace umlauts
      query = query.replace('ö', 'o')
      query = query.replace('ä', 'a')
      query = query.replace('ü', 'u')

      url = "https://www.deezer.com/ajax/gw-light.php?method=deezer.pageSearch&input=3&api_version=1.0&api_token=aVE~x_OmVc4PRLOMQ6cw8.i.3Xm4yy41&cid=85194582"

      payload = "{\"query\":\"" + query + "\",\"start\":0,\"nb\":40,\"suggest\":true,\"artist_suggest\":true,\"top_tracks\":true}"
      headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.deezer.com/search/kanye%20west',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.deezer.com',
        'Connection': 'keep-alive',
        'Cookie': 'dzr_uniq_id=dzr_uniq_id_fr562dd3991804207f5cbc53f7db6e473c1be815; consentStatistics=0; consentMarketing=0; cookieConsent=BOpFhmLOpFhmLA7ABCENAVAAAAAhF7_______9______9uz_Gv_v_f__33e8__9v_l_7_-___u_-33d4-_1vX99yfm1-7ftr3tp_86ues2_Xur_9pd3shA; dz_lang=us; G_ENABLED_IDPS=google; arl=32bd72c5e515810930c6e96e838799d06d327576fa53ccaded4ed0ecc444783dc3adef60ddaaaa8ab445bd677f673d6e5c7aecd54907dab5ae442f3f3e04615faf25a7940dde451fa59fe969b650d242d89565b80aab1dcd9f2868a6333bbe26; comeback=1; ab.storage.userId.5ba97124-1b79-4acc-86b7-9547bc58cb18=%7B%22g%22%3A%223192373864%22%2C%22c%22%3A1572199353881%2C%22l%22%3A1572199353881%7D; ab.storage.sessionId.5ba97124-1b79-4acc-86b7-9547bc58cb18=%7B%22g%22%3A%22aff07001-ab16-0f1e-fb7a-c30ebff98c82%22%2C%22e%22%3A1573675082088%2C%22c%22%3A1573672619377%2C%22l%22%3A1573673282088%7D; ab.storage.deviceId.5ba97124-1b79-4acc-86b7-9547bc58cb18=%7B%22g%22%3A%221f99170c-f7e6-f08f-6058-effaa18a33e4%22%2C%22c%22%3A1572199353883%2C%22l%22%3A1572199353883%7D; sid=frff5ec8f490d7929b5982d0240249286b49ba0b',
        'TE': 'Trailers'
      }

      response = requests.request("POST", url, headers=headers, data = payload)
      json_result = json.loads(response.text)

      # check for error
      if json_result["results"] != {}:
        if len(json_result["results"]["TRACK"]["data"]):
          first_hit = json_result["results"]["TRACK"]["data"][0]
          hits = len(json_result["results"]["TRACK"]["data"])
          # ID
          id = first_hit["SNG_ID"]
          # title
          title = first_hit["SNG_TITLE"]
          # artist
          artist = first_hit["ART_NAME"]
          # album
          album = first_hit["ALB_TITLE"]
          #print('found song:', title, 'by', artist, 'on', album)
          print('https://www.deezer.com/us/track/' + id + '/')
          #print('hits:', hits)
        else:
          print('no hit for', query)
      else:
        print('error', json_result["error"], 'for', query)