# ARTEFACTO DE AUDITORÍA OFICIAL - SENA CIMI
**Programa:** Tecnología en Análisis y Desarrollo de Software (ADSO) | **Ficha:** 3381732  
**Instructor:** John Freddy Becerra Castellanos | **Fecha:** 05-10-2026  
**Repositorio Auditado:** https://github.com/Marcosuarez02/Proyecto_bitacora_adso  
**Propietario:** Marco Antonio Suárez (`Marcosuarez02`)  
**Auditor:** Andrés Felipe Parra Aguilar (`Andresfelixx`) / Miguel Serrano Díaz (`serranodiazm3-byte`)  
**Rama:** `audit/revision-codigo`

---

## 1. MATRIZ DE EVALUACIÓN Y VALIDACIÓN (EXCEL)

| Ítem | Indicador / Variable Evaluada | Cumple | Observaciones del Auditor |
| :---: | :--- | :---: | :--- |
| **1** | Sincronización remota en GitHub con Git Flow y Conventional Commits | **SÍ** | Estructura completa de ramas `main`, `develop`, ramas `feature/...` y prefijos semánticos (`feat`, `docs`, `test`, `chore`, `fix`). |
| **2** | Vinculación del compañero auditor con permisos de escritura en GitHub | **SÍ** | Auditores vinculados activamente en Settings > Collaborators con acceso de escritura. |
| **3** | Aceptación de invitación y clonación exitosa del repositorio (`git clone`) | **SÍ** | Clonación verificada sin errores de dependencias ni ramas rotas. |
| **4** | Verificación de ramas remotas y locales con `git branch -a` | **SÍ** | Se validan ramas `main`, `develop` y las 8 ramas `feature/...` semanales. |
| **5** | Verificación de integridad del flujo de trabajo Git Flow | **SÍ** | Ciclo de vida de ramas correctamente aislado entre características y desarrollo. |
| **6** | Verificación de autoría y perfiles vinculados en GitHub | **SÍ** | Los commits reflejan la autoría real y correos verificados de los 3 integrantes. |
| **7** | Diligenciamiento completo del Artefacto de Auditoría oficial | **SÍ** | Consolidado con puntos positivos, oportunidades de mejora y hallazgos. |
| **8** | Guardado del artefacto dentro de la carpeta del proyecto | **SÍ** | Ubicado en la raíz del repositorio (`AUDITORIA.md`). |
| **9** | Commit Conventional y subida de la rama (`audit/revision-codigo`) | **SÍ** | Registrado con `docs(audit): ...` y subido exitosamente a GitHub remoto. |
| **10**| Entrega final con enlace a la rama de auditoría | **SÍ** | Enlace listo: `https://github.com/Marcosuarez02/Proyecto_bitacora_adso/tree/audit/revision-codigo`. |

---

## 2. HALLAZGOS TÉCNICOS DE LA AUDITORÍA

### A. Puntos Positivos
- Cumplimiento estricto del estándar **Conventional Commits** en el 100% de los commits históricos.
- Separación ordenada de trabajo semanal por ramas de características (`feature/julio-semana4`, `feature/agosto-semana1..3`, `feature/septiembre-semana1..4`).
- Trazabilidad colaborativa en las semanas finales con múltiples autores reconocidos por GitHub (`Contributors 3`).

### B. Acciones de Mejora
- Incluir un archivo descriptivo de arquitectura o documentación técnica en la rama principal antes de la entrega productiva.

### C. Hallazgos Críticos (Puntos Negativos)
- **Ninguno.** No se detectaron conflictos de fusión, commits huérfanos ni pérdidas de información.

---

**Estado Final de la Auditoría:** **APROBADO (10/10 CUMPLE)**  
**Firma Auditor:** Andrés Felipe Parra Aguilar / Miguel Serrano Díaz  
