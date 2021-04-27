# Video 1 - Basic Chat Application | Chat Application using Flask, Socket.IO & mongoDB (Part-1).

<br>

Na primeira parte, configuramos nosso projeto e criamos uma versão bem básica de nosso aplicativo de chat.

<https://www.riosoft.com.br/wp-content/uploads/2019/04/post_chat.png>

# Socket.IO (<https://socket.io>)

> Socket.IO é um [protocolo de transporte] (<https://github.com/socketio/socket.io-protocol>) que permite a comunicação bidirecional em tempo real baseada em eventos entre clientes (normalmente, embora nem sempre, navegadores da web) e um servidor. As implementações oficiais dos componentes cliente e servidor são escritas em **JavaScript** .

# Flask (

<www.palletsprojects.com p="" flask="">)</www.palletsprojects.com>

> Flask é uma micro estrutura da web escrita em Python. É classificado como um microframework porque não requer ferramentas ou bibliotecas particulares. Ele não tem camada de abstração de banco de dados, validação de formulário ou quaisquer outros componentes onde bibliotecas de terceiros pré-existentes fornecem funções comuns.

# flask-socketio (<https://flask-socketio.readthedocs.io/en/latest/>)

> Integração Socket.IO para aplicativos Flask. Ele é construído sobre **python-socketio** (<https://python-socketio.readthedocs.io/en/latest/>) que fornece implementações Python de um cliente e servidor Socket.IO.

# eventlet (<http://eventlet.net/>)

> Eventlet é uma biblioteca de rede simultânea para Python que permite alterar a forma como você executa seu código, não como você o escreve.

# Requirements (requisitos)

## Server (lado servidor)

```
flask
flask-socketio
eventlet
```

## Client (lado cliente)

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.3.0/socket.io.js"></script>
```
