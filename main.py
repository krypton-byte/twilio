import wikipedia,subprocess
from googletrans import Translator
from gtts import gTTS
import os,json,random,api,urllib
import requests
from flask import *
from twilio.twiml.messaging_response import *
translator = Translator()
my=Flask(__name__)
@my.route('/')
def akar():
	return '+---------------------------------+'
@my.route('/reply-sms',methods=['POST'])
def balasan():
	balas=MessagingResponse()
	chat=request.form.get('Body')
	perintah=chat.split(' ')
	if perintah[0].lower() in 'yt':
		if perintah[1]:
			dat=requests.get('https://krypton-api.herokuapp.com/api/yt',params={'url':perintah[1]}).text
			print(dat)
			js=json.loads(dat)
			url=[]
			if js['status'] == 'error':
				balas.message('error')
				return str(balas)
			else:
				md = balas.message(js['judul'])
				md.media(js['data'][0]['url'])
				return str(balas)
	elif perintah[0].lower() in ['down','download','unduh']:
		md=balas.message()
		md.media(perintah[1])
		return str(balas)
	elif perintah[0].lower() in ['git','git_clone','gits']:
		md=balas.message()
		md.media('https://codeload.github.com/%s/%s/zip/master'%(perintah[1],perintah[2]))
		return str(balas)
	elif perintah[0].lower() in ['py','python']:
		cmd=subprocess.run(["python",'-c',perintah[1:]], capture_output=True)
		if cmd.stdout.decode() == '':
			balas.message(cmd.stderr.decode())
			return str(balas)
		else:
			balas.message(cmd.stdout.decode())
			return str(balas)
	elif perintah[0].lower() in ['yt2mp3','ytmp3']:
		if perintah[1]:
			dat1=json.loads(requests.get('https://krypton-api.herokuapp.com/api/yt2mp3',params={'url':perintah[1]}).text)
			print(str(dat1))
			if dat1['status'] =='error':
				balas.message('error🙁')
				return str(balas)
			else:
				md=balas.message(dat1['judul'])
				md.media(dat1['url'])
				return str(balas)
		else:
			balas.message('yt2mp3 <url>')
			return str(balas)
	elif perintah[0].lower() in ['qrgenerator','qr-generator']:
		if perintah[1]:
			resp=json.loads(requests.get('https://krypton-api.herokuapp.com/api/QrGenerator',params={'text':' '.join(perintah[1:])}).text)
			if resp['status'] == 'sukses':
				md=balas.message('sukses')
				md.media(resp['url'])
				return str(balas)
			else:
				balas.message('gagal🙁')
				return str(balas)
		else:
			balas.message('Qr-Generator <text>')
			return str(balas)
	elif chat.split(' ')[0].lower() in ['p','₱']:
		lis=['images','images1','images2','images3']
		md=balas.message(' ')
		md.media('http://papaclash.com/sticker/%s.jpeg'%(random.choice(lis)))
		return str(balas)
	elif perintah[0].lower() == 'tts':
		cf=gTTS(text=' '.join(perintah[1:]), lang='id')
		md=balas.message('')
		md.media(cf.get_urls()[0])
		return str(balas)
	elif (perintah[0].lower() in ['kontol','ajg']):
		cf=gTTS(text='saya tidak di setting untuk berbicara tidak sehat',lang='id')
		md=balas.message('🥰')
		md.media(cf.get_urls()[0])
		return str(balas)
	elif (perintah[0].lower() in ['anjink','ajg','bgsd','babyk','babi']):
		cf=gTTS(text='saya tidak di setting untuk berbicara kasar ',lang='id')
		md=balas.message('🥰')
		md.media(cf.get_urls()[0])
		return str(balas)
	elif perintah[0].lower() in ['assalmualaikum','asalamualaikum','assalamu\'alaikum','asalamu\'alaikum','assalamualaikum']:
		cf=gTTS(text='Wa alaikumSalam Warohmatuwlohi Wabarokatuh',lang='id')
		md=balas.message('🥰')
		md.media(cf.get_urls()[0])
		return str(balas)
	elif chat.split(' ')[0].lower() in ['img-random','randomimage']:
		md=balas.message('Sukses 🤗')
		md.media('https://source.unsplash.com/collection/190727/1600x900')
		return str(balas)
	elif chat.split(' ')[0].lower() == 'url2png':
		take=api.url2png(chat.split(' ')[1])
		md=balas.message(' ')
		md.media(take)
		return str(balas)
	elif chat.split(' ')[0].lower() in ['about']:
		profile='''
+-------------------------------+
# NAMA-------: K-BOT -----------+
# DIBUAT-----: 23-MARET-2020 ---+
# DIPERBARUI-: 25-MARET-2020 ---+
# PEMBUAT----: KRYPTON-BYTE ----+
# KELOMPOK---: Clay Trial ------+
# ANGGOTA----: ~ REXY ----------+
# -----------: ~ ./KITSUNE -----+
# -----------: ~ MhankBarBar ---+
# -----------: ~ KRYPTON-BYTE --+
# -----------: ~ Maulana -------+
# -----------: ~ ripal ---------+
+-------------------------------+
'''
		md=balas.message(profile)
		md.media('http://papaclash.com/sticker/download.png')
		return str(balas)
	else:
		balas.message(reply(chat))
		return str(balas)
def reply(chat):
	perintah=chat.split(' ')
	try:
		if perintah[0] in ['menu','Menu']:
			arg='''

Author   : +6283172366463
Perintah :
	------Network Scanner-----
         ReverseIpLookup <ip>
         HttpHeader <url>
         Nmap <ip>
         ExtractLink <url>
         AsLookup <ip>
         GeoIpLookup <ip>
         Ping <url>
         MtrTraceroute <ip>
         ReverseDnsLookup <ip>
         DnsLookup <url>
         WhoIs <ip>|<url>
       ---------other------------
         Quotes
         Proxy
         Url2png <url>
         Img-random
         Tts <text>
         Translate <kalimat>
         Wikipedia <kata>
         About
         Lapor
         yt <url> <kualitas>
         yt2mp3 <url>
         QrGenerator <text>
'''
			return arg
		elif perintah[0].lower() == 'wikipedia':
			wikipedia.set_lang('id')
			v=wikipedia.page(' '.join(perintah[1:]))
			return 'judul : %s\nsumber : %s \n   %s\n\npencarian lainnya : %s'%(v.title,v.url,v.summary,'\n   ~ '.join(wikipedia.search(perintah[1:])))
		elif perintah[0] in ['ReverseIpLookup','reverseiplookup']: #ip
			return requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={perintah[1]}').text
		elif perintah[0] in ['HttpHeader','httpheader']: #url
			return requests.get(f'https://api.hackertarget.com/httpheaders/?q={perintah[1]}').text
		elif perintah[0] in ['Nmap','nmap']: #ip
			return requests.get(f'https://api.hackertarget.com/nmap/?q={perintah[1]}').text
		elif perintah[0] in ['ExtractLink','extractlink']: #url
			return requests.get(f'https://api.hackertarget.com/pagelinks/?q={perintah[1]}').text
		elif perintah[0] in ['AsLookup','aslook']: #ip
			return requests.get(f'https://api.hackertarget.com/aslookup/?q={perintah[1]}').text
		elif perintah[0] in ['GeoIpLookup','geoiplookup']: #ip
			return requests.get(f'https://api.hackertarget.com/geoip/?q={perintah[1]}').text
		elif perintah[0] in ['Ping','ping']: #url
			return requests.get(f'https://api.hackertarget.com/nping/?q={perintah[1]}').text
		elif perintah[0] in ['MtrTraceroute','mtrtraceroute']:
			return requests.get(f'https://api.hackertarget.com/mtr/?q={perintah[1]}').text
		elif perintah[0] in ['ReverseDnsLookup','reversednslookup']: #dns
			return requests.get(f'https://api.hackertarget.com/reversedns/?q={perintah[1]}').text
		elif perintah[0] in ['DnsLookup','dnslookup']: # url
			return requests.get(f'https://api.hackertarget.com/dnslookup/?q={perintah[1]}').text
		elif perintah[0] in ['WhoIs','whois']:
			return requests.get(f'https://api.hackertarget.com/whois/?q={perintah[1]}').text
		elif perintah[0].lower() == 'translate':
			arti=translator.translate(chat[len(perintah[0]):],dest='id')
			return arti.text
		elif perintah[0] in ['Quotes','quotes']:
			cv=json.loads(requests.get('https://api.quotable.io/random').text)
			arti=translator.translate(cv['content'],dest='id')
			artag=translator.translate(cv['tags'][0], dest='id')
			return 'Author : '+cv['author']+'\ntags : '+artag.text+'\n\n'+arti.text
		elif perintah[0].lower() in ['lapor','report']:
			return 'https://wa.me/+6283172366463'
		elif perintah[0] in ['Proxy','proxy']:
			vv=open('pi').read().split('\n')
			return random.choice(vv)
		else:
			res=requests.get('https://secureapp.simsimi.com/v1/simsimi/talkset?uid=287126054&av=6.8.9.4&lc=id&cc=&tz=Asia%2FJakarta&os=a&ak=pNfLbeQT%2B0cnFY8YHQb7CNHowpg%3D&message_sentence='+urllib.parse.quote(chat)+'&normalProb=8&isFilter=1&talkCnt=2&talkCntTotal=2&reqFilter=1&session=XZzaduTVCSqa6vMtuyFhGv9eCXiyWwKJVETZjpQjc2oLPGBN2XtpzcKRFhLukHd6EAYVWMiSGuPzQV5Vwcdmwz14&triggerKeywords=%5B%5D').text
			return json.loads(res)['simsimi_talk_set']['answers'][0]['sentence']
	except IndexError:
		return 'argument tidak valid ketik menu untuk menampilkan semua perintah'
if __name__ == '__main__':
	my.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)),debug=True)
