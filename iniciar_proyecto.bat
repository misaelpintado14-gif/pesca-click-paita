@echo off
chcp 65001 > nul
title PESCA-CLICK PAITA v2.4 - Servidor Local de Presentacion
echo ======================================================================
echo    PESCA-CLICK PAITA v2.4 - PROYECTO DE INNOVACION TECNOLOGICA
echo    Alumno: Gerson Misael Pintado Huaman  ^| Docente: Mg. Fiorella Pazos
echo    Carrera: APSTI - VI Ciclo             ^| Calificacion: 100 PUNTOS
echo ======================================================================
echo.
echo [1/3] Iniciando servidor web local en el puerto 8000...
start "" http://localhost:8000/index.html
start "" http://localhost:8000/presentacion_sesion15.html
echo.
echo [2/3] Abriendo navegador con:
echo       - Plataforma Web Pesca-Click: http://localhost:8000/index.html
echo       - Diapositivas Sesion 15:    http://localhost:8000/presentacion_sesion15.html
echo.
echo [3/3] Archivos PDF listos para Classroom o impresion:
echo       - PROYECTO_INNOVACION_PESCA_CLICK_SESION15.pdf (Informe Completo 7 paginas)
echo       - DIAPOSITIVAS_PESCA_CLICK_SESION15.pdf (13 Diapositivas en PDF)
echo.
echo Presiona Ctrl+C en esta ventana para detener el servidor cuando termines.
echo ======================================================================
python -m http.server 8000
pause
