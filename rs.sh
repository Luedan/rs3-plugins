#!/usr/bin/env bash
# ==============================================================================
# CLI Principal para Desarrollo de Plugins de RuneScape (Git Bash)
# ==============================================================================

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

show_help() {
    echo -e "\033[1;36m==========================================================\033[0m"
    echo -e "\033[1;36m       RuneScape Client API - CLI de Desarrollo           \033[0m"
    echo -e "\033[1;36m==========================================================\033[0m"
    echo -e "Uso: ./rs.sh [comando] [argumentos]\n"
    echo -e "Comandos disponibles:"
    echo -e "  \033[1;33msync [nombre]\033[0m       Enlaza los plugins con dev_plugins de RuneScape Beta (tiempo real)"
    echo -e "  \033[1;33mnew <id> [nombre]\033[0m   Crea un nuevo plugin listo para codificar"
    echo -e "  \033[1;33mpack <nombre>\033[0m       Valida y comprime el plugin en .zip para Mod.io"
    echo -e "  \033[1;33mlist\033[0m                Muestra todos los plugins del proyecto"
    echo -e "  \033[1;33mclean\033[0m               Elimina los enlaces en dev_plugins"
    echo -e "\nEjemplos:"
    echo -e "  ./rs.sh sync                    (Enlaza todos los plugins)"
    echo -e "  ./rs.sh sync test-plugin        (Enlaza solo test-plugin)"
    echo -e "  ./rs.sh new mi-plugin \"Mi Plugin\""
    echo -e "  ./rs.sh pack test-plugin"
    echo -e "\033[1;36m==========================================================\033[0m"
}

case "$1" in
    sync)
        shift
        "$DIR/tools/sync-plugins.sh" "$@"
        ;;
    new|create)
        shift
        "$DIR/tools/create-plugin.sh" "$@"
        ;;
    pack|package)
        shift
        "$DIR/tools/package-plugin.sh" "$@"
        ;;
    clean)
        "$DIR/tools/sync-plugins.sh" --clean
        ;;
    list)
        echo -e "\033[1;36mPlugins en el proyecto:\033[0m"
        for p in "$DIR/plugins"/*; do
            if [ -d "$p" ]; then
                pname=$(basename "$p")
                echo -e "  * \033[1;33m$pname\033[0m"
            fi
        done
        ;;
    *)
        show_help
        ;;
esac
