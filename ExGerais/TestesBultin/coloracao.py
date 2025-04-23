# Cores de texto
preto     = '\033[30m'
vermelho  = '\033[31m'
verde     = '\033[32m'
amarelo   = '\033[33m'
azul      = '\033[34m'
roxo      = '\033[35m'
ciano     = '\033[36m'
branco    = '\033[37m'

# Cores fortes (brilhantes)
preto_claro     = '\033[90m'
vermelho_claro  = '\033[91m'
verde_claro     = '\033[92m'
amarelo_claro   = '\033[93m'
azul_claro      = '\033[94m'
roxo_claro      = '\033[95m'
ciano_claro     = '\033[96m'
branco_claro    = '\033[97m'

# Estilos
negrito     = '\033[1m'
sublinhado  = '\033[4m'
inverso     = '\033[7m'

# Reset
reset       = '\033[0m'

# Fundo (background)
fundo_preto     = '\033[40m'
fundo_vermelho  = '\033[41m'
fundo_verde     = '\033[42m'
fundo_amarelo   = '\033[43m'
fundo_azul      = '\033[44m'
fundo_roxo      = '\033[45m'
fundo_ciano     = '\033[46m'
fundo_branco    = '\033[47m'

#ex
print(f"{verde}Texto verde{reset} e {vermelho}texto vermelho{reset}")
print(f"{negrito}{amarelo}Atenção!{reset}")
print(f"{fundo_azul}{branco}Texto com fundo azul{reset}")
