import freesound

c = freesound.FreesoundClient()
c.set_token("bc4e71b01652c61a22573964e885253806b31839","token")

sound = c.text_search(query=raw_input("Insert sound query: "),fields="id,name,previews")[1]

sound.retrieve_preview(".",sound.name+".mp3")
print "Downloaded "+sound.name+".mp3"