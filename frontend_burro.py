# frontend.py

import streamlit as st
from contrato import *
from datetime import datetime, time
from pydantic import ValidationError
 
# Função principal para o frontend
def main():
    st.title("Sistema de CRM e Vendas da ZapFlow - Frontend Simples")

    # Campos de entrada para os dados
    email = st.text_input("Email do Vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["ZapFlow com Gemini", "ZapFlow com chatGPT", "ZapFlow com Llama3.0"])

    # Botão de submissão
    if st.button("Salvar"):
        try:
            # Combinando a data e hora selecionadas para criar o datetime
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            # Exibindo os dados na tela
            st.write(venda)
            
        except ValidationError as e:
            st.error(f"Deu erro {e}")
            

if __name__ == "__main__":
    main()