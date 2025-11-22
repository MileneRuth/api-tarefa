from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar Flask", "status": "pendente"},
    {"id": 2, "titulo": "Criar primeira API", "status": "feito"},
]

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas), 200

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    print("DEBUG:", dados)

    if not dados or "titulo" not in dados:
        return jsonify({"erro": "Campo 'titulo' é obrigatorio"}), 400

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados["titulo"],
        "status": dados.get("status", "pendente")
    }

    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['titulo'] = dados.get('titulo',tarefa['titulo'])
            tarefa['status'] = dados.get('status',tarefa['status'])
            return jsonify(tarefa), 200
    return jsonify({"erro": "tarefa não encontrada"}), 404
    
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "tarefa deletada"}), 200
    return jsonify({"erro": "tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)