# This Python file uses the following encoding: utf-8
# Importa las librerias necesarias

import io
import json
import twitter
import datetime

# usaremos la variable now como prefijo para nombrar diferentes archivos y no reescribirlos.
now = str(datetime.datetime.now())

# XXX: vaya a http://twitter.com/apps/new a cerar una app y obtener los
# valores para las credenciales que necesitara para llenar las
# siguentes variables que están vacías
#
# En este video https://vimeo.com/79220146 explican paso a paso
# este proceso
#
# Mire https://dev.twitter.com/docs/auth/oauth para más información
# en la implementación de Twitter's OAuth.


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


# el usuario o palabra que queremos consultar

QUERY = 'innovation'

# El archivo al que grabaremos los resultados en JSON separados
# por línea y con la fecha en el nombre.
OUT_FILE = QUERY + now + ".json"

# Se autentica con Twitter

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
CONSUMER_KEY, CONSUMER_SECRET)

# Crea una conexión a la API de Streamming

twitter_stream = twitter.TwitterStream(auth=auth)

print 'Filtering the public timeline for "{0}"'.format(QUERY)

# mire https://dev.twitter.com/docs/streaming-apis en los parametros de las keywords
stream = twitter_stream.statuses.filter(track=QUERY)

# Escriba un tweet por linea en un documento JSON.

with io.open(OUT_FILE, 'w', encoding='utf-8', buffering=1) as f:
	for tweet in stream:
		f.write(unicode(u'{0}\n'.format(json.dumps(tweet, ensure_ascii=False))))
		print tweet['text']
