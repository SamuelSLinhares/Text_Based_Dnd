from .dados import d20, d12, d10, d8, d6, d4, d2

def chama_sagrada(self, target, acoes):
    resultado = (d20(1) + target.des)
    if resultado > self.cd:
        print(f"O(a) {target.nome} desviou da chama!")
    else:
        dano = d8(1)
        target.hp_atual -= dano
        print(f"O(a) {target.nome} foi atingido e tomou {dano} pontos de dano!")
    acoes.remove("A")

cantrip_registry = {
    "Chama Sagrada": (chama_sagrada, "inimigo", "A")
}

all_cantrips = set(cantrip_registry.values())