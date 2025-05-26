.PHONY: run clean

# Comando para executar o menu principal
run:
	python exemplo_menu_principal.py

# Comando para limpar arquivos temporários (se houver)
clean:
	rm -f *.pyc
	rm -rf __pycache__
