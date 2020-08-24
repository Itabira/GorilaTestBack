# GorilaTestBack

A aplicação foi hospedada [aqui](https://gorila-api-test.herokuapp.com//).
A api suporta os seguintes tipos de requisição?
  * /GET : para listar todas as transações;
  * /POST : para adicionar uma no transação no formato:
      {   "date": "2012-04-23 15:25:43.511000",
          "transaction_type": "Fixed Income",
          "value": 12985662.55
      }
  * /DELETE<id> : para deletar uma transação passando um id como parâmetro.
  

Caso queira rodar a aplicação localmente, utilize o seguinte comando:
```shell
python main.py
```
Também se encontra alguns arquivos para realização de testes.

De acordo com o roteiro, a aplicação foi codificada utilizando os seguintes componentes:

Back-end: Python, Flask, Postgresql;
Front-end: Angular;
Hospedagem: Heroku;
Autenticação: Firebase.
Agradeço pela oportunidade de fazer esse desafio. Aprendi muito durante todo o processo. Ainda há aspectos a serem melhorados mas acho que consegui entregar o resultado proposto. Fico a disposição para qualquer dúvida. Obrigado!
