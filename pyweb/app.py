from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
from entidades import Cliente, Produto
from clienteDao import ClienteDao
from favoritosDao import FavoritoDao
from produtoDao import ProdutoDao

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wow1001'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/reset_db", methods=["GET"])
def reset_db():
    from database import Database
    Database.create_db()
    dao = ProdutoDao()
    dao.import_csv()
    flash(f'Banco de dados Resetado', 'success')
    return redirect(url_for("cliente_index"))


# ==================================
# ROTAS (CLIENTE)
# ==================================

@app.route("/cliente/edit/<id>", methods=["GET"])
def cliente_edit(id):
    dao = ClienteDao()
    cliente = dao.get_cliente(id)
    return render_template("cliente.html",
                           cliente=cliente,
                           action='update'
                           )


@app.route("/cliente/index", methods=["GET"])
def cliente_index():
    dc = ClienteDao()
    clientes = dc.find_all()
    return render_template("cliente_list.html", clientes=clientes)


@app.route("/cliente/new", methods=["GET"])
def cliente_new():
    return render_template("cliente.html",
                           action='create',
                           cliente=None)

# -------
# CRUD
# -------

# CREATE


@app.route("/cliente/create", methods=["POST"])
def cliente_create():

    nome = request.form.get("nome")
    cep = request.form.get("cep")
    email = request.form.get("email")
    cpf = request.form.get("cpf")

    cliente = Cliente(nome, email, cep=cep, cpf=cpf)

    dao = ClienteDao()
    dao.save(cliente)

    # retornar feedback para o usuário
    flash(f'Cliente "{nome}" cadastrado!', 'success')

    return redirect(url_for("cliente_index"))

# DELETE


@app.route("/cliente/delete/<id>", methods=["GET"])
def cliente_delete(id):
    dao = ClienteDao()
    dao.delete(id)
    flash(f'Cliente removido com sucesso!', 'success')
    return redirect(url_for('cliente_index'))


# READ
@app.route("/cliente/<id>", methods=["GET"])
def cliente_id(id):
    # dc = ClienteDao()
    # cliente = dc.get_cliente(id)
    # return cliente.__dict__
    return "<h1>TODO: implementar</h1>"


# UPDATE
@app.route("/cliente/update", methods=["POST"])
def cliente_update():

    dao = ClienteDao()
    # obtem o id que foi setado no form
    id = request.form.get("id")

    # obtem o cliente que esta no banco
    cliente = dao.get_cliente(id)

    # atualiza os campos do cliente (todos os campos)
    cliente.nome = request.form.get("nome")
    cliente.cep = request.form.get("cep")
    cliente.email = request.form.get("email")
    cliente.cpf = request.form.get("cpf")

    dao.update(cliente)

    # retornar feedback para o usuário
    flash(f'Cliente "{cliente.nome}" Atualizado!', 'success')

    return redirect(url_for("cliente_index"))

# ==================================
# ROTAS (Favoritos)
# ==================================


@app.route("/favoritos/index", methods=["GET"])
def favoritos_index():
    dc = FavoritoDao()
    produtos = dc.find_all()
    return render_template("favoritos_list.html", produtos=produtos)


@app.route("/produto/remover_favorito", methods=["GET"])
def remover_favorito():
    dao = ProdutoDao()
    produto_id = request.args.get('produtoID')
    dao.remover_favorito(produto_id)
    flash(f'Produto tirado dos favoritos com sucesso!', 'success')
    return redirect(url_for('favoritos_index'))

# ==================================
# ROTAS (PRODUTO)
# ==================================


@app.route("/produto/busca", methods=["POST"])
def busca_produto():
    dao = ProdutoDao()
    nome = request.form.get("nome")
    produtos = dao.busca_produto(nome)
    return render_template("produto_list.html", produtos=produtos)


@app.route("/produto/favoritar/<id>", methods=["GET"])
def favoritar(id):
    dao = ProdutoDao()
    produto = dao.favoritar(id)
    return redirect(url_for('favoritos_index'))


@app.route("/produto/create", methods=["POST"])
def produto_create():
    nome = request.form.get("nome")
    categoria = request.form.get("categoria")
    preco = request.form.get("preco")

    produto = Produto(nome, categoria, preco)

    dao = ProdutoDao()
    dao.save(produto)

    # retornar feedback para o usuário
    flash(f'Produto "{nome}" cadastrado!', 'success')

    return redirect(url_for("produto_index"))


# DELETE
@app.route("/produto/delete/<id>", methods=["GET"])
def produto_delete(id):
    dao = ProdutoDao()
    dao.delete(id)
    flash(f'Produto removido com sucesso!', 'success')
    return redirect(url_for('produto_index'))


@app.route("/produto/edit/<id>", methods=["GET"])
def produto_edit(id):
    dao = ProdutoDao()
    produto = dao.get_produto(id)
    return render_template("produto.html",
                           produto=produto,
                           action='update'
                           )

# READ


@app.route("/produto/<id>", methods=["GET"])
def produto_id(id):
    dc = ProdutoDao()
    produto = dc.get_produto(id)
    return produto


@app.route("/produto/index", methods=["GET"])
def produto_index():
    dc = ProdutoDao()
    produtos = dc.find_all()
    return render_template("produto_list.html", produtos=produtos)


@app.route("/produto/new", methods=["GET"])
def produto_new():
    return render_template("produto.html",
                           action='create',
                           produto=None)


# UPDATE
@app.route("/produto/update", methods=["POST"])
def produto_update():

    dao = ProdutoDao()
    # obtem o id que foi setado no form
    id = request.form.get("id")

    # obtem o produto que esta no banco
    produto = dao.get_produto(id)

    # atualiza os campos do produto (todos os campos)
    produto.nome = request.form.get("nome")
    produto.categoria = request.form.get("categoria")
    produto.preco = request.form.get("preco")

    dao.update(produto)

    # retornar feedback para o usuário
    flash(f'Produto "{produto.nome}" Atualizado!', 'success')

    return redirect(url_for("produto_index"))


if __name__ == "__main__":
    app.run(debug=True)
