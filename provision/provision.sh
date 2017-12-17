vagrant up --provider=aws

fab -i /Users/mrmedfac9/Downloads/KEY.pem -H ubuntu@DNS instalarProyecto
fab -i /Users/mrmedfac9/Downloads/KEY.pem -H ubuntu@DNS subirApi