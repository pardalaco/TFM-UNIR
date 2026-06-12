![](media/image1.png){width="4.2034722222222225in"
height="0.9458333333333333in"}

Universidad Internacional de La Rioja

Escuela Superior de Ingeniería y Tecnología

Máster Universitario en Ciberseguridad

EVMAudit: Librería multiherramienta para la detección automatizada de
vulnerabilidades en contratos inteligentes de Ethereum

+-------------------------------+----------------------------------+
| Trabajo fin de estudio        | Adrián Moreno Martín             |
| presentado por:               |                                  |
|                               | Daniel Rovira Martínez           |
|                               |                                  |
|                               | Paula Suárez Prieto              |
+===============================+==================================+
| Tipo de trabajo:              | Desarrollo de software           |
+-------------------------------+----------------------------------+
| Director/a:                   | Friman Sánchez Castaño           |
+-------------------------------+----------------------------------+
| Fecha:                        | 22/04/2026                       |
+-------------------------------+----------------------------------+

Resumen

La seguridad de los contratos inteligentes se ha convertido en un
aspecto crítico dentro del ecosistema blockchain debido al elevado
impacto económico que pueden provocar las vulnerabilidades presentes en
este tipo de software. Aunque existen herramientas especializadas para
su análisis, como Slither, Mythril o Echidna, sus resultados suelen
presentarse de forma heterogénea y con dificultades para correlacionar y
priorizar los hallazgos obtenidos. En este Trabajo Fin de Máster se
presenta EVMAudit, una librería desarrollada en Python orientada a la
ejecución conjunta de múltiples herramientas de análisis de seguridad
para contratos inteligentes compatibles con la Ethereum Virtual Machine
(EVM). La solución propuesta incorpora mecanismos de normalización,
correlación y priorización de resultados, permitiendo ofrecer una visión
unificada y más estructurada de las vulnerabilidades detectadas. Además,
la herramienta se distribuye mediante PyPI y dispone de una
infraestructura de despliegue y automatización basada en Docker y CI/CD.

Palabras clave: contratos inteligentes, Ethereum, ciberseguridad,
análisis de vulnerabilidades, blockchain

Abstract

Smart contract security has become a critical concern within the
blockchain ecosystem due to the significant economic impact caused by
software vulnerabilities. Although several specialized analysis tools,
such as Slither, Mythril, and Echidna, are available, their results are
often heterogeneous and difficult to correlate and prioritize. This
Master\'s Thesis presents EVMAudit, a Python library designed to
orchestrate multiple security analysis tools for Ethereum Virtual
Machine (EVM) compatible smart contracts. The proposed solution includes
mechanisms for result normalization, correlation, and prioritization,
providing a unified and more structured view of the detected
vulnerabilities. Furthermore, the tool is distributed through PyPI and
includes an automated deployment infrastructure based on Docker and
CI/CD practices.

Keywords: smart contracts, Ethereum, cybersecurity, vulnerability
analysis, blockchain

Índice de contenidos

Tabla de contenido

[1. Introducción [1](#introducción)](#introducción)

[1.1. Motivación [2](#motivación)](#motivación)

[1.2. Planteamiento del problema
[2](#planteamiento-del-problema)](#planteamiento-del-problema)

[1.3. Estructura del trabajo
[3](#estructura-del-trabajo)](#estructura-del-trabajo)

[2. Estado del arte [4](#estado-del-arte)](#estado-del-arte)

[2.1. Fundamentos blockchain y contratos inteligentes
[4](#fundamentos-blockchain-y-contratos-inteligentes)](#fundamentos-blockchain-y-contratos-inteligentes)

[2.1.1. Tipos de redes blockchain
[5](#tipos-de-redes-blockchain)](#tipos-de-redes-blockchain)

[2.1.2. Consenso entre nodos
[5](#consenso-entre-nodos)](#consenso-entre-nodos)

[2.1.3. Fundamentos de contratos inteligentes
[7](#fundamentos-de-contratos-inteligentes)](#fundamentos-de-contratos-inteligentes)

[2.1.4. Ethereum Virtual Machine
[7](#ethereum-virtual-machine)](#ethereum-virtual-machine)

[2.1.5. Propiedades de los contratos inteligentes
[8](#propiedades-de-los-contratos-inteligentes)](#propiedades-de-los-contratos-inteligentes)

[2.1.6. Limitaciones y riesgos
[8](#limitaciones-y-riesgos)](#limitaciones-y-riesgos)

[2.1.7. Aplicaciones descentralizadas (DApps)
[8](#aplicaciones-descentralizadas-dapps)](#aplicaciones-descentralizadas-dapps)

[2.2. Finanzas Descentralizadas (DeFi): ecosistema y riesgo estructural
[9](#finanzas-descentralizadas-defi-ecosistema-y-riesgo-estructural)](#finanzas-descentralizadas-defi-ecosistema-y-riesgo-estructural)

[2.3. Interoperabilidad blockchain: bridges y protocolos cross-chain
[10](#interoperabilidad-blockchain-bridges-y-protocolos-cross-chain)](#interoperabilidad-blockchain-bridges-y-protocolos-cross-chain)

[2.3.1. El problema de las blockchains aisladas
[10](#el-problema-de-las-blockchains-aisladas)](#el-problema-de-las-blockchains-aisladas)

[2.3.2. Tipos de bridges y arquitecturas
[11](#tipos-de-bridges-y-arquitecturas)](#tipos-de-bridges-y-arquitecturas)

[2.3.3. Componentes técnicos de un bridge
[12](#componentes-técnicos-de-un-bridge)](#componentes-técnicos-de-un-bridge)

[2.4. Herramientas de Análisis
[13](#herramientas-de-análisis)](#herramientas-de-análisis)

[2.4.1. Slither [13](#slither)](#slither)

[2.4.2. Mythril --- Ejecución Simbólica (ConsenSys)
[15](#mythril-ejecución-simbólica-consensys)](#mythril-ejecución-simbólica-consensys)

[2.4.3. Echidna --- Fuzzing Basado en Propiedades (Trail of Bits)
[17](#echidna-fuzzing-basado-en-propiedades-trail-of-bits)](#echidna-fuzzing-basado-en-propiedades-trail-of-bits)

[2.5. Vulnerabilidades de seguridad en contratos inteligentes de
Ethereum
[18](#vulnerabilidades-de-seguridad-en-contratos-inteligentes-de-ethereum)](#vulnerabilidades-de-seguridad-en-contratos-inteligentes-de-ethereum)

[2.5.1. Vulnerabilidades técnicas de ejecución
[19](#vulnerabilidades-técnicas-de-ejecución)](#vulnerabilidades-técnicas-de-ejecución)

[2.5.2. Vulnerabilidades de control y privilegios
[19](#vulnerabilidades-de-control-y-privilegios)](#vulnerabilidades-de-control-y-privilegios)

[2.5.3. Vulnerabilidades económicas y dependencia del entorno
[20](#vulnerabilidades-económicas-y-dependencia-del-entorno)](#vulnerabilidades-económicas-y-dependencia-del-entorno)

[2.5.4. Errores lógicos de negocio
[20](#errores-lógicos-de-negocio)](#errores-lógicos-de-negocio)

[2.5.5. Conclusión [20](#conclusión)](#conclusión)

[2.6. Ataques Reales [22](#ataques-reales)](#ataques-reales)

[2.6.1. Vulnerabilidad técnica de ejecución: The DAO (2016)
[22](#vulnerabilidad-técnica-de-ejecución-the-dao-2016)](#vulnerabilidad-técnica-de-ejecución-the-dao-2016)

[2.6.2. Vulnerabilidad de control y privilegios: Poly Network (2021)
[23](#vulnerabilidad-de-control-y-privilegios-poly-network-2021)](#vulnerabilidad-de-control-y-privilegios-poly-network-2021)

[2.6.3. Vulnerabilidad económica y dependencia del entorno: bZx (2020)
[23](#vulnerabilidad-económica-y-dependencia-del-entorno-bzx-2020)](#vulnerabilidad-económica-y-dependencia-del-entorno-bzx-2020)

[2.6.4. Error lógico de negocio: Euler Finance (2023)
[25](#error-lógico-de-negocio-euler-finance-2023)](#error-lógico-de-negocio-euler-finance-2023)

[2.7. Síntesis y limitaciones del estado del arte
[25](#síntesis-y-limitaciones-del-estado-del-arte)](#síntesis-y-limitaciones-del-estado-del-arte)

[3. Objetivos concretos y metodología de trabajo
[27](#objetivos-concretos-y-metodología-de-trabajo)](#objetivos-concretos-y-metodología-de-trabajo)

[3.1. Objetivo general [27](#objetivo-general)](#objetivo-general)

[3.2. Objetivos específicos
[27](#objetivos-específicos)](#objetivos-específicos)

[3.3. Metodología del trabajo
[27](#metodología-del-trabajo)](#metodología-del-trabajo)

[4. Desarrollo específico de la contribución
[29](#desarrollo-específico-de-la-contribución)](#desarrollo-específico-de-la-contribución)

[4.1. Identificación de requisitos
[29](#identificación-de-requisitos)](#identificación-de-requisitos)

[4.2. Descripción de la herramienta software desarrollada
[30](#descripción-de-la-herramienta-software-desarrollada)](#descripción-de-la-herramienta-software-desarrollada)

[4.2.1. Módulo 1: Ejecución de herramientas (evmaudit.runner)
[32](#módulo-1-ejecución-de-herramientas-evmaudit.runner)](#módulo-1-ejecución-de-herramientas-evmaudit.runner)

[4.2.2. Módulo 2: Normalización (evmaudit.normalizer)
[35](#módulo-2-normalización-evmaudit.normalizer)](#módulo-2-normalización-evmaudit.normalizer)

[4.2.3. Módulo 3: Correlación (evmaudit.correlator)
[37](#módulo-3-correlación-evmaudit.correlator)](#módulo-3-correlación-evmaudit.correlator)

[4.2.4. Módulo 4: Priorización (evmaudit.prioritizer)
[40](#módulo-4-priorización-evmaudit.prioritizer)](#módulo-4-priorización-evmaudit.prioritizer)

[4.2.5. Módulo 5: Generación de informes (evmaudit.reporter)
[42](#módulo-5-generación-de-informes-evmaudit.reporter)](#módulo-5-generación-de-informes-evmaudit.reporter)

[4.2.6. Identificación de requisitos
[45](#identificación-de-requisitos-1)](#identificación-de-requisitos-1)

[4.2.7. Descripción de la herramienta software desarrollada
[45](#descripción-de-la-herramienta-software-desarrollada-1)](#descripción-de-la-herramienta-software-desarrollada-1)

[4.2.8. Evaluación [45](#evaluación)](#evaluación)

[5. Conclusiones y trabajo futuro
[46](#conclusiones-y-trabajo-futuro)](#conclusiones-y-trabajo-futuro)

[5.1. Conclusiones [46](#conclusiones)](#conclusiones)

[5.2. Trabajo futuro [46](#trabajo-futuro)](#trabajo-futuro)

[Referencias bibliográficas
[47](#referencias-bibliográficas)](#referencias-bibliográficas)

[Anexo A. Ejemplos de vulnerabilidades en contratos inteligentes
[51](#ejemplos-de-vulnerabilidades-en-contratos-inteligentes)](#ejemplos-de-vulnerabilidades-en-contratos-inteligentes)

[Anexo B. Entorno virtual Python
[58](#entorno-virtual-python)](#entorno-virtual-python)

[5.2.1. ¿Por qué usar entornos virtuales?
[58](#por-qué-usar-entornos-virtuales)](#por-qué-usar-entornos-virtuales)

[5.2.2. Tipos de entornos virtuales
[59](#tipos-de-entornos-virtuales)](#tipos-de-entornos-virtuales)

[5.2.3. Herramienta a usar: uv
[60](#herramienta-a-usar-uv)](#herramienta-a-usar-uv)

[Anexo C. Distribución y Publicación en el Registro de Paquetes PyPI
[62](#distribución-y-publicación-en-el-registro-de-paquetes-pypi)](#distribución-y-publicación-en-el-registro-de-paquetes-pypi)

[5.2.4. Configuración de Metadatos del Proyecto (pyproject.toml)
[62](#configuración-de-metadatos-del-proyecto-pyproject.toml)](#configuración-de-metadatos-del-proyecto-pyproject.toml)

[5.2.5. Proceso de Compilación del Paquete
[63](#proceso-de-compilación-del-paquete)](#proceso-de-compilación-del-paquete)

[5.2.6. Seguridad y Autenticación en la Publicación
[63](#seguridad-y-autenticación-en-la-publicación)](#seguridad-y-autenticación-en-la-publicación)

[5.2.7. Ejecución del Despliegue
[65](#ejecución-del-despliegue-1)](#ejecución-del-despliegue-1)

[5.2.8. Ciclo de Mantenimiento y Actualización de Versiones
[65](#ciclo-de-mantenimiento-y-actualización-de-versiones)](#ciclo-de-mantenimiento-y-actualización-de-versiones)

[Anexo D. Entorno de Integración Continua (CI/CD) y Publicación
Automatizada
[67](#entorno-de-integración-continua-cicd-y-publicación-automatizada)](#entorno-de-integración-continua-cicd-y-publicación-automatizada)

[5.2.9. Arquitectura del Workflow y Disparadores (*Triggers*)
[67](#arquitectura-del-workflow-y-disparadores-triggers)](#arquitectura-del-workflow-y-disparadores-triggers)

[5.2.10. Desglose Técnico de las Etapas del Pipeline
[67](#desglose-técnico-de-las-etapas-del-pipeline)](#desglose-técnico-de-las-etapas-del-pipeline)

[Anexo E. Aplicación web desarrollada
[70](#aplicación-web-desarrollada)](#aplicación-web-desarrollada)

[Anexo F. Contenedorización e Infraestructura de Despliegue (Docker)
[71](#contenedorización-e-infraestructura-de-despliegue-docker)](#contenedorización-e-infraestructura-de-despliegue-docker)

Índice de figuras

[Figura 1. *Cadena genérica de bloques*
[4](#_Toc230713172)](#_Toc230713172)

[Figura 2. *Pipeline EVMAudit* [30](#_Toc230713173)](#_Toc230713173)

Índice de tablas

[Tabla 1. *Organización del trabajo en
grupo.*[VIII](#_Toc150422790)](#_Toc150422790)

[Tabla 2. *Ejemplo de tabla con sus principales elementos.*[**¡Error!
Marcador no definido.**](#_Toc150422791)](#_Toc150422791)

Organización del trabajo en grupo

En este apartado se detallarán las distintas partes en las que se ha
dividido el trabajo entre los componentes del grupo, los objetivos
perseguidos en cada una de ellas y los mecanismos de coordinación
empleados. Este apartado deberá ser validado por el director para poder
comenzar con el trabajo.

Partes que aborda el TFE, distribución y estructura de la memoria

+-----------------------------------------------------------------------------------+
| Organización del trabajo en grupo - Desarrollo de la memoria                      |
+=============================================+=====================================+
| Apartado de la memoria                      | Responsables                        |
+---------------------------------------------+-------------------------------------+
| Introducción                                | Alumno 1, Alumno 2 y Alumno 3       |
+---------------------------------------------+-------------------------------------+
| Estado del arte                             | Alumno 1, Alumno 2 y Alumno 3       |
+---------------------------------------------+-------------------------------------+
| Objetivos y metodología de trabajo          | Alumno 1, Alumno 2 y Alumno 3       |
+---------------------------------------------+-------------------------------------+
| Desarrollo específico de la contribución:   | Alumno 1                            |
| parte individual 1                          |                                     |
+---------------------------------------------+-------------------------------------+
| Desarrollo específico de la contribución:   | Alumno 2                            |
| parte individual 2                          |                                     |
+---------------------------------------------+-------------------------------------+
| Desarrollo específico de la contribución:   | Alumno 3                            |
| parte individual 3                          |                                     |
+---------------------------------------------+-------------------------------------+
| Desarrollo específico de la contribución:   | Alumno 1, Alumno 2 y Alumno 3       |
| parte 4                                     |                                     |
+---------------------------------------------+-------------------------------------+
| Conclusiones y trabajo futuro               | Alumno 1, Alumno 2 y Alumno 3       |
+---------------------------------------------+-------------------------------------+

: []{#_Toc150422790 .anchor}Tabla 1. Organización del trabajo en grupo.

Fuente: Elaboración propia.

Mecanismos de coordinación empleados

Con el objetivo de garantizar un seguimiento continuo del trabajo y
mantener la coordinación entre los miembros del grupo, se estableció una
reunión interna semanal en la que cada integrante exponía las tareas
realizadas durante el periodo correspondiente y las posibles
dificultades encontradas. Estas reuniones permitían, además, debatir las
siguientes líneas de trabajo y planificar las tareas a desarrollar en
las semanas posteriores.

Como herramientas de comunicación y colaboración se utilizaron
principalmente WhatsApp para la comunicación diaria, Microsoft Teams
para la realización de reuniones telemáticas, un repositorio compartido
en GitHub para la gestión y sincronización del código fuente, y un
documento compartido de Microsoft Word para la elaboración conjunta de
la memoria.

Adicionalmente, tras cada una de las entregas parciales previstas en la
planificación del Trabajo Fin de Máster, se mantuvo una reunión de
seguimiento con el director del trabajo. Estas sesiones permitieron
revisar el progreso realizado, recibir retroalimentación sobre los
resultados obtenidos y definir las acciones necesarias para las
siguientes fases del proyecto.

# Introducción 

La tecnología blockchain ha evolucionado significativamente desde la
aparición de Bitcoin en 2008 como sistema de dinero electrónico
descentralizado. Con la llegada de plataformas como Ethereum, blockchain
dejó de utilizarse únicamente para la transferencia de activos digitales
y pasó a convertirse en una infraestructura capaz de ejecutar
aplicaciones descentralizadas mediante contratos inteligentes. Estos
contratos permiten automatizar lógica de negocio y gestionar activos sin
necesidad de intermediarios, lo que ha impulsado el crecimiento de
sectores como las finanzas descentralizadas (DeFi), los sistemas de
tokenización y los protocolos de interoperabilidad blockchain.

Sin embargo, este nuevo paradigma también introduce importantes desafíos
desde el punto de vista de la ciberseguridad. Los contratos inteligentes
operan en entornos públicos y adversariales, donde el código es
accesible para cualquier usuario y los errores pueden ser analizados y
explotados por actores maliciosos. Además, la inmutabilidad de la
blockchain dificulta la corrección de vulnerabilidades una vez
desplegados los contratos, aumentando el impacto potencial de cualquier
fallo de seguridad.

Durante los últimos años, múltiples incidentes han demostrado las
consecuencias reales de estas vulnerabilidades. Ataques como The DAO,
Poly Network, bZx o Euler Finance provocaron pérdidas económicas de
cientos de millones de dólares y evidenciaron que los errores en
contratos inteligentes no solo afectan al software, sino también a
activos digitales con valor económico directo.

En este contexto, el análisis de seguridad de contratos inteligentes se
ha convertido en una de las áreas más relevantes dentro de la
ciberseguridad blockchain. Actualmente existen distintas herramientas
especializadas que permiten detectar vulnerabilidades mediante técnicas
como análisis estático, ejecución simbólica o fuzzing. No obstante,
estas soluciones presentan limitaciones importantes, entre las que
destacan la elevada tasa de falsos positivos, la fragmentación de
resultados y la dificultad para priorizar riesgos de manera efectiva.

El presente Trabajo Fin de Máster se centra en el diseño e
implementación de una librería en Python orientada al análisis de
seguridad de contratos inteligentes compatibles con la Ethereum Virtual
Machine (EVM). La propuesta busca integrar distintas herramientas de
análisis existentes en una arquitectura modular capaz de correlacionar
hallazgos, normalizar resultados heterogéneos y facilitar una evaluación
más útil y estructurada de las vulnerabilidades detectadas.

La finalidad del trabajo no es reemplazar las herramientas actuales,
sino proporcionar una capa adicional de correlación y análisis que
mejore la interpretación de resultados y reduzca algunas de las
limitaciones presentes en el estado del arte. Para ello, se estudiarán
las principales técnicas de auditoría de smart contracts, las
vulnerabilidades más relevantes en Solidity y las herramientas más
utilizadas en entornos profesionales y académicos.

Finalmente, el trabajo incluirá el diseño de la arquitectura de la
solución propuesta, su implementación como librería software y una
evaluación experimental utilizando contratos vulnerables conocidos y
casos reales de código abierto.

## Motivación

La auditoría de contratos inteligentes se ha convertido en una necesidad
crítica dentro del ecosistema blockchain debido al creciente volumen
económico gestionado por aplicaciones descentralizadas y protocolos
DeFi. En este contexto, la detección temprana de vulnerabilidades
resulta fundamental para reducir riesgos de explotación y minimizar
pérdidas económicas.

Actualmente existen diversas herramientas orientadas al análisis
automatizado de contratos inteligentes, como Slither, Mythril o Echidna,
que aplican técnicas de análisis diferentes y complementarias. Sin
embargo, su utilización conjunta continúa presentando dificultades
relevantes. Cada herramienta genera resultados con formatos, niveles de
detalle y criterios de severidad distintos, lo que dificulta la
correlación de hallazgos y obliga a realizar revisiones manuales
adicionales durante el proceso de auditoría.

Además, muchas soluciones actuales producen un elevado número de falsos
positivos o detectan vulnerabilidades redundantes, complicando la
priorización efectiva de riesgos. Esta situación provoca que los
auditores deban invertir una cantidad significativa de tiempo en
interpretar resultados y validar manualmente la relevancia real de cada
hallazgo.

La motivación principal de este trabajo surge de la necesidad de mejorar
este proceso mediante una solución que permita integrar y normalizar
información procedente de múltiples herramientas de análisis. Se busca
proporcionar una visión más estructurada y útil del estado de seguridad
de un contrato inteligente, facilitando tanto la interpretación de
resultados como la identificación de vulnerabilidades relevantes.

Desde el punto de vista académico y profesional, el trabajo también
pretende contribuir al estudio de técnicas de análisis aplicadas a
contratos inteligentes y explorar enfoques que permitan mejorar la
automatización de auditorías de seguridad en entornos blockchain.

## Planteamiento del problema

El análisis de seguridad de contratos inteligentes presenta dificultades
específicas derivadas tanto del modelo de ejecución de blockchain como
de las limitaciones de las herramientas actuales de auditoría
automática.

Por un lado, los contratos inteligentes operan en un entorno
especialmente adversarial. El código fuente y el bytecode suelen ser
públicos, las transacciones son observables y los atacantes pueden
estudiar el comportamiento interno de los contratos antes de explotar
una vulnerabilidad. Además, la ejecución determinista de la Ethereum
Virtual Machine y la inmutabilidad del despliegue implican que muchos
errores no puedan corregirse fácilmente una vez publicados en la red.

Por otro lado, las herramientas automáticas de análisis existentes
presentan limitaciones relevantes. Soluciones ampliamente utilizadas
como Slither, Mythril o Echidna aplican técnicas diferentes y generan
resultados heterogéneos tanto en formato como en nivel de detalle. Esto
provoca problemas como:

- Detección redundante de una misma vulnerabilidad por múltiples
  herramientas.

- Generación de falsos positivos.

- Dificultad para correlacionar hallazgos relacionados.

- Ausencia de criterios homogéneos de priorización.

- Escasa contextualización del impacto real de las vulnerabilidades.

Como consecuencia, los procesos de auditoría continúan dependiendo en
gran medida de la revisión manual realizada por expertos, especialmente
para validar resultados y diferenciar vulnerabilidades críticas de
hallazgos con impacto reducido.

Ante esta situación, el problema abordado en este trabajo consiste en
cómo mejorar el análisis automatizado de contratos inteligentes mediante
un sistema capaz de integrar múltiples herramientas de seguridad,
normalizar sus resultados y proporcionar una visión más estructurada y
útil de las vulnerabilidades detectadas.

Para ello, se propone el desarrollo de una librería en Python orientada
a la correlación de hallazgos de seguridad en contratos inteligentes
compatibles con la EVM, utilizando un enfoque modular que facilite la
integración de distintas técnicas de análisis.

## Estructura del trabajo

El presente documento se organiza en varios capítulos que permiten
abordar de forma progresiva tanto el contexto teórico del problema como
el desarrollo de la solución propuesta.

En primer lugar, el capítulo de introducción presenta el contexto
general del trabajo, la motivación del estudio y el problema
identificado.

A continuación, el capítulo correspondiente al estado del arte recoge
los fundamentos necesarios para comprender el análisis de seguridad en
contratos inteligentes. En este apartado se abordan conceptos
relacionados con blockchain, Ethereum, contratos inteligentes, así como
las principales vulnerabilidades de seguridad, técnicas de auditoría y
herramientas de análisis existentes en la actualidad.

Posteriormente, el capítulo de objetivos concretos y metodología de
trabajo define el objetivo general del TFM, los objetivos específicos y
las distintas fases planteadas para el desarrollo de la solución
propuesta. También se describe el enfoque metodológico utilizado para la
investigación, diseño, implementación y validación del sistema.

El capítulo de desarrollo específico de la contribución constituye el
núcleo principal del trabajo. En él se describe el diseño e
implementación de la librería desarrollada, incluyendo la arquitectura
del sistema, los módulos principales, la integración de herramientas
externas, el proceso de normalización y correlación de resultados y los
mecanismos de evaluación empleados.

Finalmente, el capítulo de conclusiones y trabajo futuro recoge las
principales aportaciones del trabajo, las limitaciones identificadas
durante el desarrollo y posibles líneas de mejora o evolución futura de
la herramienta propuesta.

# Estado del arte

El presente capítulo recoge los fundamentos técnicos y el contexto
necesario para comprender el problema abordado en este Trabajo Fin de
Máster. En primer lugar, se introducen los conceptos básicos de
blockchain y contratos inteligentes, con especial atención a Ethereum y
al modelo de ejecución de la Ethereum Virtual Machine. Posteriormente,
se analizan los principales retos de seguridad asociados a los contratos
inteligentes, las vulnerabilidades más frecuentes, los ataques reales
más representativos y las herramientas actuales de análisis. Finalmente,
se identifican las limitaciones del estado del arte que justifican el
desarrollo de una librería en Python orientada a la integración y
correlación de resultados de seguridad.

## Fundamentos blockchain y contratos inteligentes

La tecnología ***blockchain*** se define como un sistema de registro
distribuido (*distributed ledger*) que permite almacenar y gestionar
información de forma descentralizada, segura y resistente a
manipulaciones, sin depender de una autoridad central de confianza. Este
paradigma fue introducido por Satoshi Nakamoto en 2008, en el contexto
del diseño de Bitcoin, donde se propone un sistema de dinero
electrónico *peer-to-peer* basado en un libro mayor compartido entre
múltiples nodos de la red. \[1\]

En una blockchain, las transacciones se agrupan en estructuras
denominadas **bloques**, que se enlazan secuencialmente mediante
**funciones hash criptográficas**. Cada bloque contiene, entre otros
elementos, un conjunto de transacciones validadas, una marca temporal y
el hash del bloque anterior. Este encadenamiento garantiza la integridad
del sistema, ya que cualquier modificación en un bloque previamente
confirmado alteraría su hash, rompiendo la continuidad de la cadena y
permitiendo detectar manipulaciones de forma inmediata. \[2\]

![[]{#_Toc230713172 .anchor}Figura 1. *Cadena genérica de
bloques*](media/image2.png){width="6.299305555555556in"
height="1.9208333333333334in"}

Fuente: Blockchain Technology Overview, NISTIR 8202.

Adicionalmente, blockchain emplea criptografía asimétrica para asegurar
la autenticidad e integridad de las transacciones. Cada participante
dispone de un par de claves criptográficas (clave pública y clave
privada), donde la clave privada se utiliza para firmar digitalmente las
transacciones, y la clave pública permite a otros nodos verificar su
validez. Este mecanismo elimina la necesidad de intermediarios de
confianza, trasladando la verificación al propio sistema distribuido.
\[2\]

###  Tipos de redes blockchain

Las redes blockchain pueden clasificarse en función de su modelo de
acceso y gobernanza, distinguiéndose principalmente entre redes públicas
(*permissionless*) y redes privadas (*permissioned*).

Las ***blockchains** **permisionless*** permiten la participación
abierta de cualquier usuario, que puede leer el estado del *ledger* y,
dependiendo del protocolo de consenso, participar en la validación de
bloques. Este modelo prioriza la descentralización, la transparencia y
la resistencia a la censura. Ejemplos representativos
incluyen Bitcoin y Ethereum.

Por otro lado, las ***blockchains** **permissioned*** restringen el
acceso a un conjunto predefinido de participantes autorizados. En este
contexto, los nodos validadores son conocidos y controlados, lo que
permite optimizar el rendimiento, reducir el coste computacional y
facilitar el cumplimiento de requisitos regulatorios. Sin embargo, este
modelo introduce un mayor grado de centralización. Un ejemplo
ampliamente adoptado en entornos empresariales es Hyperledger Fabric.

En términos generales, las redes públicas priorizan la transparencia y
la descentralización, mientras que las redes privadas favorecen la
eficiencia operativa, el control y la privacidad, lo que explica su
adopción en contextos corporativos. \[2\]

###  Consenso entre nodos

Uno de los problemas fundamentales en sistemas distribuidos consiste en
lograr que un conjunto de nodos alcance un acuerdo sobre el estado del
sistema, incluso en presencia de fallos o comportamientos maliciosos.
Este problema ha sido ampliamente estudiado en la literatura, destacando
el trabajo de Leslie Lamport junto con Shostak y Pease, quienes
formalizaron el consenso en entornos con fallos arbitrarios mediante
el *Byzantine Generals Problem*, sentando las bases de la tolerancia a
fallos bizantinos (*Byzantine Fault Tolerance*, BFT). \[3\]

En este contexto, un sistema tolerante a fallos bizantinos debe ser
capaz de alcanzar consenso incluso cuando algunos nodos presentan
comportamientos maliciosos o arbitrarios, como el envío de información
falsa o la manipulación deliberada del protocolo. Este modelo resulta
especialmente relevante en redes abiertas y sin permisos, como las
blockchain públicas, donde no existe una relación de confianza previa
entre los participantes.

No obstante, no todos los algoritmos de consenso contemplan este modelo
adversarial. Protocolos clásicos como *Paxos Protocol* están diseñados
para entornos con fallos por parada (*crash faults*), en los que los
nodos pueden fallar o dejar de responder, pero no actúan de forma
maliciosa. Esta limitación los hace inadecuados para escenarios abiertos
como blockchain, donde se asume la posible existencia de actores
maliciosos. \[4\]

A partir de estos fundamentos, las redes blockchain han desarrollado
mecanismos de consenso específicos que permiten mantener la coherencia
del sistema en entornos descentralizados y potencialmente hostiles.
\[2\]Entre los más relevantes destacan:

- **Proof of Work (PoW)**: basado en la resolución de problemas
  criptográficos que requieren un elevado coste computacional. Este
  mecanismo, utilizado por Bitcoin, proporciona seguridad al hacer
  económicamente inviable la manipulación de la cadena, aunque presenta
  limitaciones en términos de eficiencia energética y escalabilidad.

- **Proof of Stake (PoS)**: sustituye el esfuerzo computacional por la
  participación económica, donde los validadores son seleccionados en
  función de la cantidad de activos bloqueados (*stake*). Este enfoque
  mejora la eficiencia energética, pero introduce nuevos riesgos, como
  la concentración de poder o ataques derivados del
  problema *nothing-at-stake*.

- **Delegated Proof of Stake (DPoS)**: variante de PoS en la que los
  validadores son elegidos mediante mecanismos de votación. Aumenta el
  rendimiento del sistema, aunque reduce el grado de descentralización.

- **Proof of Authority (PoA)**: modelo en el que un conjunto limitado de
  nodos autorizados valida las transacciones. Se utiliza principalmente
  en blockchains privadas, donde la identidad de los participantes es
  conocida.

Cada uno de estos mecanismos implica distintos compromisos entre
seguridad, descentralización y rendimiento, lo que en la literatura se
describe frecuentemente como un conjunto de *trade-offs* inherentes al
diseño de sistemas blockchain, comúnmente denominado el "trilema de
blockchain". \[5\], \[6\]

Desde una perspectiva de ciberseguridad, la elección del protocolo de
consenso no solo condiciona la arquitectura del sistema, sino también su
superficie de ataque. En particular, estos compromisos influyen
directamente en la viabilidad de vectores de explotación como ataques
del 51%, censura de transacciones o manipulación del orden de ejecución
(*front-running*), especialmente en entornos abiertos y sin permisos.

###  Fundamentos de contratos inteligentes

Los **contratos inteligentes** (*smart contracts*) constituyen una
extensión funcional de la tecnología blockchain que permite la ejecución
de lógica programable de forma descentralizada. El concepto fue
introducido por Nick Szabo en 1994, quien los definió como "un protocolo
de transacción informatizado que ejecuta los términos de un contrato"
\[7\]

En la actualidad, los contratos inteligentes se materializan como
programas desplegados en una red blockchain que encapsulan tanto lógica
como estado persistente. Su ejecución es llevada a cabo por los nodos de
la red, los cuales deben alcanzar un resultado determinista e idéntico
para garantizar la coherencia global del sistema. Este requisito impone
restricciones relevantes en el diseño del software, especialmente en lo
relativo al uso de fuentes externas de información o funciones no
deterministas.

Cabe destacar que no todas las plataformas blockchain soportan contratos
inteligentes. Redes como Bitcoin incorporan un lenguaje de scripting
limitado, diseñado para priorizar la seguridad y la simplicidad,
mientras que otras plataformas como Ethereum permiten la ejecución de
código arbitrario, habilitando así el desarrollo de aplicaciones
complejas sobre la blockchain. \[8\]

### Ethereum Virtual Machine

La adopción generalizada de contratos inteligentes se consolidó con la
aparición de Ethereum, que introduce un entorno de ejecución específico
denominado ***Ethereum Virtual Machine* (EVM)**. Esta máquina virtual
permite la ejecución de código de propósito general dentro de un entorno
distribuido y determinista.

El funcionamiento interno de Ethereum se describe formalmente en
el *Yellow Paper*, elaborado por Gavin Wood, donde se definen:

- La arquitectura y semántica de la EVM

- El modelo de ejecución de contratos y transacciones

- El sistema de gas como mecanismo de control de recursos

La EVM es una máquina virtual basada en pila (*stack-based*), donde cada
operación tiene un coste asociado en gas. Este mecanismo permite limitar
el consumo de recursos computacionales y actúa como protección frente a
ataques de denegación de servicio, al imponer un coste económico a la
ejecución de operaciones complejas o potencialmente abusivas. \[9\]

### Propiedades de los contratos inteligentes

Desde un punto de vista técnico, los contratos inteligentes presentan
una serie de propiedades fundamentales\[2\]:

- **Determinismo**: la ejecución debe producir el mismo resultado en
  todos los nodos, garantizando la coherencia del sistema distribuido.

- **Inmutabilidad**: una vez desplegados, los contratos no pueden
  modificarse directamente, lo que dificulta la corrección de errores.

- **Transparencia**: en redes públicas, el código y el estado del
  contrato son accesibles, favoreciendo la auditabilidad.

- **Ejecución descentralizada**: no existe un punto único de control,
  eliminando dependencias de entidades centrales.

### Limitaciones y riesgos

A pesar de sus ventajas, los contratos inteligentes presentan
importantes desafíos desde el punto de vista de la ciberseguridad \[2\]:

- **Vulnerabilidades en el código**: errores de implementación pueden
  derivar en fallos críticos explotables.

- **Problemas de control de acceso**: una gestión incorrecta de permisos
  puede permitir operaciones no autorizadas.

- **Dependencia de oráculos externos**: introduce confianza en terceros
  y posibles vectores de manipulación.

- **Inmutabilidad del código**: dificulta la corrección de
  vulnerabilidades tras el despliegue.

- **Costes de ejecución**: el modelo de gas puede ser explotado para
  provocar condiciones de denegación de servicio.

Estas características hacen que los errores en contratos inteligentes
puedan tener consecuencias críticas, como la pérdida irreversible de
activos digitales. \[2\], \[10\]

### Aplicaciones descentralizadas (DApps)

Sobre la base del modelo de ejecución, las propiedades y las
limitaciones descritas, los contratos inteligentes permiten la
construcción de aplicaciones descentralizadas (*Decentralized
Applications*, DApps), que constituyen sistemas completos en los que la
lógica de negocio se implementa parcial o totalmente mediante contratos
inteligentes. \[11\]

A diferencia de las aplicaciones tradicionales basadas en arquitecturas
cliente-servidor, las DApps distribuyen la lógica entre múltiples nodos
de la red, eliminando intermediarios y reduciendo la dependencia de
entidades centralizadas. Este cambio implica una redefinición del modelo
de confianza, donde los usuarios depositan su confianza en el código
ejecutado en la blockchain y en las garantías del protocolo subyacente.

Desde la perspectiva de la ciberseguridad, este paradigma introduce
implicaciones relevantes. La transparencia del código facilita su
auditoría, pero también permite a actores maliciosos analizarlo en busca
de vulnerabilidades. Asimismo, la composición de múltiples contratos y
la dependencia de servicios externos amplían la superficie de ataque,
pudiendo dar lugar a vulnerabilidades complejas en sistemas
interconectados, como ocurre en el ecosistema DeFi.

Además, la inmutabilidad de los contratos implica que los errores no
pueden corregirse fácilmente tras su despliegue, lo que incrementa el
impacto potencial de cualquier vulnerabilidad explotada. \[12\]

## Finanzas Descentralizadas (DeFi): ecosistema y riesgo estructural

Las finanzas descentralizadas, conocidas por su acrónimo en inglés
*DeFi* (*Decentralized Finance*), constituyen un conjunto de
aplicaciones y protocolos financieros construidos sobre redes blockchain
públicas que permiten ofrecer diversos servicios financieros entre los
que destacan: préstamos, intercambios de activos, emisión de derivados,
gestión de rendimientos... sin la intervención de intermediarios
centralizados como bancos, brokers o cámaras de compensación \[13\]. A
diferencia del sistema financiero tradicional, en el que la confianza
recae sobre instituciones reguladas y supervisadas por autoridades, en
DeFi la lógica de negocio queda codificada íntegramente en contratos
inteligentes desplegados en la cadena, accesibles públicamente y
ejecutados de forma determinista por la red sin posibilidad de
intervención posterior \[13\]\[14\].

El origen del término suele situarse en torno a 2018, aunque el concepto
tomó relevancia real a partir del fenómeno conocido como *DeFi Summer*
en 2020, cuando el valor total bloqueado (*Total Value Locked*, TVL) en
protocolos de este tipo pasó de apenas 1.000 millones de dólares a
superar los 15.000 millones en pocos meses\[13\]. En el pico del ciclo
alcista de 2021, el TVL global llegó a superar los 180.000 millones de
dólares, lo que convirtió al ecosistema DeFi en uno de los entornos de
mayor concentración de activos digitales del mundo y, en consecuencia,
en uno de los objetivos más atractivos para actores maliciosos \[14\].

La infraestructura de DeFi se organiza en torno a cuatro categorías de
protocolos fundamentales \[13\]. Los *exchanges* descentralizados (DEX)
permiten el intercambio de activos sin custodia centralizada, utilizando
modelos de *market maker* automatizado (AMM) en los que la liquidez es
aportada por los propios usuarios a través de fondos comunes. Los
protocolos de préstamo y depósito, como Aave o Compound, permiten a los
usuarios obtener crédito colateralizado o depositar activos para obtener
rendimiento, con tipos de interés determinados algorítmicamente en
función de la oferta y la demanda. Los protocolos de derivados y activos
sintéticos, como Synthetix, permiten la exposición a precios de activos
del mundo real sin necesidad de su custodia. Finalmente, los agregadores
de rendimiento automatizan estrategias de inversión combinando múltiples
protocolos en una única operación.

Todos estos protocolos comparten una característica importante desde el
punto de vista de la seguridad: gestionan directamente activos
económicos reales mediante contratos inteligentes inmutables o de
difícil actualización, lo que convierte cualquier vulnerabilidad en un
riesgo de pérdida irreversible de fondos \[14\].

## Interoperabilidad blockchain: bridges y protocolos cross-chain

###  El problema de las blockchains aisladas

El ecosistema blockchain no es un sistema unificado, sino un conjunto de
redes independientes con arquitecturas, lenguajes de contrato, modelos
de consenso y activos nativos distintos. Ethereum concentra la mayor
parte de la liquidez DeFi, pero redes como BNB Chain, Solana, Avalanche,
Polygon o Arbitrum cuentan con ecosistemas propios de considerable
tamaño e importancia económica. Esta fragmentación responde en parte a
la búsqueda de propiedades específicas (mayor rendimiento, menores
costes de transacción o mayor privacidad) que ninguna cadena única ha
logrado ofrecer de forma simultánea con suficiente madurez \[15\].

Sin embargo, la coexistencia de múltiples redes introduce un problema
estructural: por diseño, una blockchain es un sistema cerrado que opera
bajo sus propias reglas de consenso y no tiene capacidad para verificar
de forma nativa el estado de otra cadena \[15\]. Un nodo de Ethereum no
puede comprobar directamente si una transacción ha ocurrido en Solana ni
si un activo ha sido bloqueado en BNB Chain. Esta limitación, conocida
en la literatura como el problema de la comunicación entre *ledgers*
distribuidos, impide que los activos y la información fluyan libremente
entre redes sin recurrir a mecanismos intermediarios \[15\]\[16\]

Las consecuencias prácticas de esta fragmentación son significativas. La
liquidez se encuentra dispersa entre múltiples cadenas, lo que encarece
las operaciones para los usuarios y reduce la eficiencia del mercado.
Los usuarios que desean aprovechar oportunidades en distintas redes se
ven obligados a recurrir a *exchanges* centralizados o a mecanismos de
transferencia que introducen costes, demoras y, en muchos casos, riesgos
adicionales. En respuesta a esta problemática, la industria ha
desarrollado una categoría de protocolos conocidos como bridges o
puentes cross-chain, cuya función es permitir la transferencia de
activos e información entre blockchains heterogéneas \[15\]\[16\].

Zamyatin et al. formalizan este problema en su trabajo seminal sobre
comunicación entre ledgers distribuidos, estableciendo que cualquier
protocolo de interoperabilidad debe garantizar propiedades de seguridad
como la atomicidad (la transferencia ocurre por completo o no ocurre) y
la consistencia (el estado de ambas cadenas refleja correctamente la
operación realizada) \[15\]. Su análisis concluye que cumplir estas
propiedades de forma simultánea en un entorno sin confianza requiere
suposiciones criptográficas o de confianza que constituyen,
precisamente, los puntos de fragilidad del sistema.

### Tipos de bridges y arquitecturas

La literatura clasifica los bridges según dos dimensiones
complementarias: el mecanismo de transferencia que utilizan y el modelo
de confianza sobre el que se apoyan \[15\]\[16\]. Esta clasificación es
relevante no solo desde el punto de vista técnico, sino también desde la
perspectiva de la seguridad, ya que distintos diseños implican distintas
superficies de ataque y distintos supuestos de confianza.

Desde el punto de vista del mecanismo de transferencia, los modelos
principales son cuatro.

El **modelo *Lock-and-Mint***, el más extendido en la práctica, bloquea
los activos en un contrato de custodia en la cadena de origen y acuña
tokens representativos en la cadena de destino. Cuando el usuario desea
recuperar sus activos originales, los tokens representativos son
destruidos y el contrato de custodia libera los activos bloqueados. Este
modelo es sencillo de implementar, pero introduce un riesgo de
concentración: el contrato de custodia en la cadena de origen se
convierte en un punto crítico que concentra los activos de todos los
usuarios \[16\].

El **modelo *Burn-and-Mint*** elimina la necesidad de custodia
centralizada destruyendo los tokens en la cadena de origen antes de
acuñar equivalentes en la cadena de destino. Esto requiere que el token
cuente con contratos de emisión desplegados en ambas cadenas con
autoridad para quemar y acuñar. Los *Atomic Swaps* permiten intercambios
directos entre cadenas mediante contratos de tiempo bloqueado (*Hash
Time-Locked Contracts*, HTLC), que garantizan que la transferencia es
atómica sin necesidad de custodia de terceros, aunque con limitaciones
de liquidez y compatibilidad entre cadenas \[15\]. Finalmente, las
*Liquidity Networks* utilizan pools de liquidez pre-fondeados en cada
cadena para facilitar las transferencias, reduciendo los tiempos de
espera a costa de requerir capital inmovilizado en ambos extremos.

Desde el punto de vista del modelo de confianza, Belchior et al.
establecen una taxonomía en cuatro niveles \[16\]. Los bridges
custodiales o centralizados confían en una única entidad que custodia
los activos bloqueados y autoriza las acuñaciones en la cadena destino,
lo que los hace rápidos y sencillos pero equivalentes en términos de
riesgo a un *exchange* centralizado. Los bridges basados en *multisig*
distribuyen la autorización entre un conjunto de validadores,
requiriendo que un umbral mínimo de ellos firme cada operación; su
seguridad depende directamente del número de validadores, su
independencia y la protección de sus claves privadas. Los bridges con
*light clients* eliminan la necesidad de confiar en validadores externos
verificando pruebas criptográficas del estado de la cadena de origen
directamente en el contrato de la cadena de destino, lo que los hace más
seguros, pero también más complejos y costosos en términos de gas. Los
*ZK-bridges*, el estado del arte actual, utilizan pruebas de
conocimiento cero para demostrar matemáticamente la corrección de las
*transacciones cross-chain* sin revelar información adicional,
ofreciendo garantías de seguridad muy superiores, si bien su adopción
generalizada aún está limitada por la complejidad computacional de
generación de pruebas \[16\].

### Componentes técnicos de un bridge

Con independencia del modelo concreto adoptado, los bridges comparten
una serie de componentes técnicos cuya correcta implementación es
determinante para su seguridad \[15\]\[16\].

Los contratos inteligentes de bloqueo y acuñación constituyen el núcleo
del bridge en la capa *on-chain*. En la cadena de origen, un contrato
recibe y custodia los activos del usuario, emitiendo un evento que sirve
como prueba de la operación. En la cadena de destino, un segundo
contrato recibe la prueba verificada y acuña los activos
representativos. La lógica de estos contratos debe implementar
correctamente las comprobaciones de autorización, los mecanismos de
verificación de pruebas y las condiciones de reversión ante situaciones
anómalas \[15\].

Los validadores o *relayers* son los componentes que operan fuera de la
cadena y cuya función es detectar eventos en la cadena de origen,
construir las pruebas correspondientes y enviarlas al contrato de la
cadena de destino. En *bridges multisig*, cada validador firma
independientemente la prueba de la operación, y el contrato de destino
verifica que se ha alcanzado el umbral de firmas requerido antes de
ejecutar la acuñación. La seguridad de este componente depende en gran
medida de la gestión de claves privadas de los validadores y de la
distribución del conjunto validador \[16\].

Los sistemas de verificación de pruebas son el mecanismo mediante el
cual el contrato de la cadena de destino comprueba que la operación
declarada por el *relayer* ha ocurrido realmente en la cadena de origen.
Según la arquitectura del bridge, esta verificación puede basarse en la
comprobación de un umbral de firmas de validadores autorizados, en la
verificación de una prueba Merkle sobre el estado de la cadena de
origen, o en la verificación de una prueba criptográfica de conocimiento
cero. La corrección de este componente es crítica: un fallo en la lógica
de verificación puede permitir a un atacante fabricar pruebas falsas y
acuñar activos sin respaldo \[15\].

Finalmente, los mecanismos de seguridad complementarios incluyen
sistemas de límites de transferencia por período de tiempo, funciones de
pausa de emergencia, esquemas de *timelock* para operaciones de
actualización del protocolo y sistemas de monitorización *on-chain*.
Aunque estos mecanismos no eliminan las vulnerabilidades subyacentes,
pueden limitar el impacto de un exploit al reducir la ventana de tiempo
durante la cual un atacante puede extraer fondos antes de que el
protocolo sea pausado \[16\].

La combinación de todos estos componentes hace que los bridges sean
sistemas de complejidad técnica considerablemente superior a la de un
contrato DeFi convencional. Operan simultáneamente en múltiples entornos
de ejecución heterogéneos, dependen de componentes *off-chain* con sus
propios vectores de compromiso, y gestionan volúmenes de activos que los
convierten en objetivos de alto valor económico. Esta combinación de
complejidad, heterogeneidad y concentración de activos explica por qué
los bridges han concentrado algunas de las pérdidas más significativas
de la historia del ecosistema blockchain, y por qué su análisis de
seguridad plantea desafíos específicos que trascienden las capacidades
de las herramientas de análisis de contratos inteligentes actualmente
disponibles \[17\]. Las vulnerabilidades concretas que afectan a estos
sistemas, así como los ataques reales que las han materializado, se
analizan en los apartados siguientes de este estado del arte.

## Herramientas de Análisis

### Slither

#### Descripción y características principales

Slither es un framework de análisis estático de código abierto diseñado
específicamente para la evaluación de seguridad de contratos
inteligentes desarrollados en Solidity y Vyper. En la actualidad, se
posiciona como una de las herramientas más robustas y ampliamente
adoptadas tanto en el ámbito académico como en la industria de la
auditoría de protocolos descentralizados.

Desarrollado por la firma de seguridad Trail of Bits, su presentación
formal tuvo lugar en 2019 a través del artículo de investigación
Slither: A Static Analysis Framework For Smart Contracts \[18\], cuyos
autores son Josselin Feist, Gustavo Grieco y Alex Groce

Arquitectura y Funcionamiento

El núcleo de Slither está implementado en Python y su principal ventaja
competitiva reside en su flujo de análisis. A diferencia de otras
herramientas que operan directamente sobre el bytecode de la Ethereum
Virtual Machine (EVM), Slither recupera el Árbol de Sintaxis Abstracta
(AST) de los contratos y lo traduce a una representación intermedia
propia denominada SlithIR.

Esta representación, basada en *Static Single Assignment* (SSA), permite
realizar análisis de flujo de datos y de control con una precisión
elevada, facilitando la detección de vulnerabilidades complejas que los
*linters* convencionales suelen omitir.

#### Capacidades y Características Principales

De acuerdo con sus especificaciones técnicas y su repositorio oficial
\[19\], Slither ofrece un conjunto de funcionalidades críticas para el
desarrollo seguro:

- **Detección de Vulnerabilidades:** Capacidad para identificar código
  vulnerable con una tasa reducida de falsos positivos, documentada en
  una extensa lista de \"trofeos\" (vulnerabilidades reales detectadas
  en protocolos principales).

- **Trazabilidad:** Localiza con exactitud el punto del código fuente
  donde se produce la condición de error, facilitando la remediación
  inmediata.

- **Integración en el Ciclo de Vida del Software (DevSecOps):** Se
  integra de forma nativa en entornos de desarrollo como Hardhat y
  Foundry, además de permitir su implementación en flujos de Integración
  Continua (CI) y escaneo de código en GitHub.

- **Herramientas de Visualización (Printers):** Incluye funciones
  integradas para generar informes rápidos sobre la información crucial
  del contrato (jerarquía de herencia, permisos, etc.).

- **Extensibilidad:** Dispone de una API de detección que permite a los
  investigadores programar análisis personalizados y detectores
  específicos en Python.

- **Rendimiento y Compatibilidad:**

  - Soporte para contratos en Solidity desde la versión 0.4 en adelante.

  - Capacidad de procesamiento del 99.9% del código público de Solidity.

  - Tiempo de ejecución promedio inferior a 1 segundo por contrato, lo
    que lo hace ideal para despliegues a gran escala.

#### Impacto en la Seguridad de Contratos Inteligentes

La importancia de Slither radica en su equilibrio entre velocidad y
precisión. Al operar sobre SlithIR, la herramienta puede realizar
análisis semánticos profundos sin la carga computacional que requieren
los motores de ejecución simbólica, permitiendo una validación constante
durante la fase de desarrollo del contrato.

#### Limitaciones de Slither

A pesar de su eficiencia, Slither presenta limitaciones propias del
análisis estático que deben ser consideradas. La herramienta no modela
interacciones complejas entre múltiples contratos de forma dinámica, lo
que le impide detectar vulnerabilidades de lógica económica, como la
manipulación de oráculos o ataques de \_flash loans\_. Asimismo, en
entornos de código con alta complejidad, múltiples niveles de herencia o
uso de ensamblador (\_inline assembly\_), Slither suele generar una tasa
elevada de falsos positivos. Esto requiere que el auditor realice una
validación manual exhaustiva para distinguir las vulnerabilidades reales
de las falsas alarmas detectadas por el software.

#### Empresas y organizaciones que lo utilizan

En el sector de la seguridad blockchain, Slither se ha consolidado como
una herramienta de referencia. Es utilizada de manera sistemática por
firmas de auditoría líderes como ConsenSys Diligence**,** Sigma Prime y
OpenZeppelin para realizar el triaje inicial de los contratos. Además,
su integración en flujos de trabajo de integración continua (CI/CD) es
un estándar en los protocolos DeFi más relevantes, entre los que
destacan Aave**,** Uniswap**,** Yearn Finance y Compound. Estas
organizaciones emplean el *framework* para automatizar el escaneo de
seguridad en cada actualización de sus repositorios antes del despliegue
definitivo en la red.\[20\], \[21\], \[22\]

### Mythril --- Ejecución Simbólica (ConsenSys)

#### Descripción y características principales

Mythril es una herramienta de seguridad de código abierto diseñada para
el análisis profundo de contratos inteligentes que se ejecutan en la
Ethereum Virtual Machine (EVM). A diferencia de los analizadores
estáticos convencionales, Mythril se categoriza como un motor de
ejecución simbólica, capaz de evaluar la seguridad de los contratos
tanto a nivel de código fuente (Solidity) como directamente sobre el
bytecode de la EVM \[23\]. Su propósito principal es identificar estados
del contrato que podrían conducir a vulnerabilidades críticas mediante
la exploración de rutas de ejecución que no son evidentes mediante la
simple lectura del código.\[24\]

#### Arquitectura y Funcionamiento

El núcleo de Mythril se basa en la ejecución simbólica con resolución
SMT (*Satisfiability Modulo Theories*)**.** Su funcionamiento se puede
desglosar en tres fases técnicas:

- **Desensamblado y Grafo de Flujo de Control (CFG):** Mythril
  descompone el *bytecode* en instrucciones de la EVM y construye un
  grafo que representa todos los caminos posibles que puede tomar una
  transacción.

- **Exploración de Estados Simbólicos:** En lugar de usar valores fijos
  (ej. enviar 1 ETH), utiliza variables simbólicas (x). La herramienta
  \"ejecuta\" el contrato de forma virtual, acumulando restricciones
  matemáticas sobre estas variables a medida que atraviesa bifurcaciones
  condicionales (if, require).

- **Resolución mediante Z3:** Para determinar si un estado vulnerable es
  alcanzable, Mythril consulta a Z3, un potente probador de teoremas
  desarrollado por Microsoft Research. Si el *solver* encuentra un
  conjunto de valores que satisfacen las condiciones para un ataque (por
  ejemplo, que el saldo sea cero y el llamante no sea el propietario),
  Mythril confirma la existencia de la vulnerabilidad.

#### Capacidades y Características Principales

En cuanto a su potencial técnico, Mythril sobresale por su capacidad
para identificar fallos lógicos de alta complejidad que están
estrechamente vinculados a la manipulación del estado de la cadena de
bloques.

Entre sus funciones más destacadas se encuentra la detección
especializada de vulnerabilidades críticas, tales como la reentrancia
clásica, el uso indebido de la instrucción DELEGATECALL, las
dependencias de *timestamp* y los desbordamientos de enteros (*integer
overflows/underflows*), estos últimos especialmente relevantes en
contratos desarrollados con versiones de Solidity anteriores a la 0.8.

Asimismo, la herramienta ofrece una versatilidad notable mediante su
funcionalidad de análisis de Mainnet, la cual permite recuperar el
bytecode directamente desde un nodo de Ethereum; esto facilita la
auditoría de contratos que ya han sido desplegados incluso si el código
fuente original no está disponible.

Finalmente, una de sus características más valoradas por los auditores
es la generación detallada de trazas de ejecución, ya que el sistema no
se limita a reportar la existencia de un error, sino que reconstruye la
secuencia exacta de transacciones necesaria para recrear el exploit y
validar la vulnerabilidad.

#### Limitaciones Técnicas

A pesar de su robustez, Mythril enfrenta desafíos significativos
derivados de la naturaleza de la ejecución simbólica. El obstáculo más
crítico es la denominada explosión de caminos (*path explosion*), un
fenómeno que ocurre en contratos con estructuras de control muy
ramificadas o bucles complejos. En estos escenarios, el número de
estados posibles aumenta de forma exponencial, lo que deriva
frecuentemente en un consumo excesivo de memoria o en la interrupción
del proceso por tiempo de espera (*timeout*) antes de completar el
análisis.\[25\]

A esta limitación estructural se suma una tasa considerable de falsos
positivos, la cual se estima en estudios independientes entre el 45% y
el 52%. Esta imprecisión suele deberse a que la herramienta, para
mantener la viabilidad del cálculo, simplifica ciertos aspectos del
entorno de la blockchain, como el estado de contratos externos o
variables ambientales complejas, lo que puede llevar a reportar
vulnerabilidades que no son explotables en un entorno real.\[26\]

Finalmente, el rendimiento operativo de Mythril es notablemente inferior
al de los analizadores estáticos como Slither. Debido a la carga
computacional que requiere la resolución de fórmulas matemáticas
mediante SMT, los tiempos de ejecución oscilan entre los 5 y 300
segundos por contrato. Esta demora depende directamente de la
profundidad de exploración configurada, lo que lo hace menos ágil para
procesos de integración continua que requieren una respuesta inmediata.

#### Ecosistema y Adopción

En la actualidad, Mythril se consolida como un pilar fundamental dentro
de la industria de la seguridad blockchain. Su relevancia técnica y
trayectoria lo han posicionado como el motor central de **MythX**, la
plataforma de análisis de seguridad profesional bajo modelo SaaS
desarrollada por ConsenSys. Esta integración permite a los
desarrolladores acceder a las capacidades de Mythril directamente desde
sus entornos de trabajo habituales.

Asimismo, la herramienta se ha convertido en un estándar dentro de los
flujos de trabajo de **auditoría profesional**. Firmas de prestigio
internacional, tales como **ConsenSys Diligence** y **Halborn**, emplean
Mythril de forma sistemática para complementar sus revisiones manuales,
utilizando su capacidad de exploración de estados para detectar errores
lógicos que podrían pasar desapercibidos en una lectura convencional del
código.

Más allá del sector comercial, Mythril posee una fuerte presencia en la
**comunidad académica**. Su naturaleza de código abierto y su
arquitectura basada en el *solver* Z3 lo convierten en una base
tecnológica recurrente para investigaciones avanzadas. Es utilizado
frecuentemente en estudios sobre verificación formal y en el desarrollo
de nuevos protocolos de seguridad destinados a proteger el ecosistema de
las finanzas descentralizadas (DeFi) \[24\], \[25\].

### Echidna --- Fuzzing Basado en Propiedades (Trail of Bits)

#### Descripción y características principales

Echidna es una herramienta de código abierto desarrollada por Trail of
Bits, diseñada específicamente para el análisis de seguridad de
contratos inteligentes en Ethereum mediante la técnica de *fuzzing*
basado en propiedades. A diferencia de las pruebas unitarias
tradicionales, que se limitan a verificar resultados ante entradas
específicas, este marco de trabajo busca falsar invariantes o predicados
definidos por el usuario, permitiendo identificar fallos lógicos
complejos que suelen pasar desapercibidos en procesos de testeo
convencionales. Implementado en Haskell, el programa destaca por su
facilidad de uso, ya que no requiere configuraciones complejas ni el
despliegue previo de los contratos en una red local.\[27\]

#### Arquitectura y Funcionamiento

El funcionamiento de Echidna se fundamenta en la generación de campañas
de *fuzzing* basadas en gramática, utilizando el ABI (*Application
Binary Interface*) del contrato para interactuar con él. El flujo de
trabajo comienza cuando el desarrollador define propiedades de seguridad
en el código Solidity, normalmente funciones con el prefijo echidna\_
que deben devolver siempre un valor booleano verdadero. A partir de
estas definiciones, la herramienta ejecuta millones de secuencias de
transacciones aleatorias y sofisticadas con el objetivo de alcanzar un
estado del contrato que rompa dichas reglas.\[28\]

#### Capacidades y Características Principales

Una de las capacidades más potentes de este fuzzer es su capacidad de
reducción de casos de prueba. Cuando Echidna detecta una violación de
una propiedad o una aserción de Solidity, el sistema realiza una
simplificación automática para reportar la secuencia mínima de
transacciones necesaria para reproducir el error. Esta eficiencia en la
detección y reporte ha quedado demostrada en entornos reales de
producción; ya en la fecha de publicación de su *paper* original, la
herramienta había sido validada con éxito en más de diez auditorías de
seguridad de gran escala, consolidándose como un estándar en el
ecosistema de seguridad de *smart contracts*.\[27\]

#### Limitaciones Técnicas

A pesar de su eficacia, Echidna presenta restricciones técnicas
inherentes a su metodología de prueba. En primer lugar, la calidad del
análisis depende de la calidad de las propiedades definidas por el
usuario; si el desarrollador no define correctamente los invariantes,
Echidna no podrá identificar fallos de lógica específicos \[29\].

Por otro lado, la herramienta puede enfrentar problemas de rendimiento
en contratos con funciones extremadamente costosas en términos de gas o
con estructuras de datos ineficientes, lo que ralentiza la generación de
transacciones \[28\].

Asimismo, aunque es excelente para detectar errores lógicos, tiene
dificultades para analizar contratos que dependen de condiciones
externas muy específicas de la red que no pueden ser fácilmente
simuladas en su entorno local de pruebas\[29\].

#### Ecosistema y Adopción

Debido a su eficacia demostrada, Echidna se ha convertido en una
herramienta estándar en la industria:

- **Trail of Bits:** Como creadores de la herramienta, la utilizan en
  todas sus auditorías de alto perfil para protocolos DeFi \[28\].

- **Auditores Profesionales:** Firmas de ciberseguridad blockchain
  emplean Echidna para validar la robustez de protocolos antes de su
  despliegue en la red principal \[29\].

- **Equipos de Desarrollo:** Proyectos de infraestructura y finanzas
  descentralizadas integran Echidna en sus tuberías de **Integración
  Continua (CI/CD)** para garantizar que cada actualización de código
  mantenga los invariantes de seguridad \[27\].

## Vulnerabilidades de seguridad en contratos inteligentes de Ethereum

Los contratos inteligentes en Ethereum presentan un modelo de seguridad
distinto al del software tradicional. Su ejecución es pública, el código
es accesible y cualquier error puede ser analizado y explotado por
actores con incentivos económicos directos. Además, la inmutabilidad
dificulta la corrección de fallos una vez desplegado el contrato, y la
interacción con otros contratos y servicios externos incrementa la
superficie de ataque. \[10\], \[30\]

Por este motivo, una vulnerabilidad en Solidity no debe entenderse solo
como un error de programación, sino como una debilidad explotable en un
entorno adversarial. En la práctica, los problemas de seguridad no se
limitan a fallos técnicos, sino que también incluyen errores de diseño y
de lógica de negocio. \[31\]

Para su análisis, resulta útil agrupar las vulnerabilidades en cuatro
categorías principales:

- Vulnerabilidades técnicas de ejecución

- Vulnerabilidades de control y privilegios

- Vulnerabilidades económicas y dependencia del entorno

- Errores lógicos de negocio

### Vulnerabilidades técnicas de ejecución

Este grupo incluye errores directamente relacionados con la ejecución en
la EVM y la implementación en Solidity.

Una de las más conocidas es la **reentrancy**, que ocurre cuando un
contrato realiza una llamada externa antes de actualizar su estado
interno. Esto permite que el contrato receptor vuelva a ejecutar la
función vulnerable con un estado inconsistente. A pesar de que existen
patrones de mitigación bien conocidos, sigue siendo una de las
vulnerabilidades más relevantes en Ethereum. \[32\]

Otra categoría importante son los **problemas aritméticos**, como
overflow y underflow. Aunque Solidity 0.8 introduce comprobaciones
automáticas, estos errores siguen siendo relevantes en contratos
antiguos, en bloques unchecked o en cálculos financieros incorrectos.

También destacan las **llamadas externas inseguras**, ya que
cualquier call transfiere el control de ejecución a otro contrato. Esto
puede provocar comportamientos inesperados o ejecución de lógica
maliciosa. En esta línea, el uso de delegatecall es especialmente
crítico, ya que ejecuta código externo sobre el almacenamiento del
contrato llamador, pudiendo comprometer completamente su estado. \[30\]

Por último, los **ataques de denegación de servicio (DoS)** son
frecuentes en este entorno. No buscan tumbar el sistema, sino bloquear
funciones críticas, por ejemplo, mediante bucles no acotados o
reversiones provocadas por contratos externos. \[30\]

### Vulnerabilidades de control y privilegios

Muchas vulnerabilidades reales no se deben a errores técnicos complejos,
sino a problemas en el control de acceso.

Esto incluye funciones sensibles sin restricciones, roles mal definidos
o privilegios excesivos. Un error típico es permitir que cualquier
usuario ejecute funciones críticas como transferencias de fondos o
cambios de configuración. \[33\]

Un caso especialmente problemático es el uso de tx.origin para
autenticación. Este valor representa el origen externo de la
transacción, no el llamador inmediato, lo que permite ataques mediante
contratos intermedios.

También son relevantes los problemas en contratos upgradeables,
especialmente los relacionados con inicializadores. Si una
función initialize no está correctamente protegida, un atacante puede
ejecutarla y asumir el control del contrato. \[34\]

### Vulnerabilidades económicas y dependencia del entorno

En muchos casos, el problema no está en el código en sí, sino en cómo
interactúa el contrato con su entorno.

El ejemplo más claro es el **front-running**, donde un atacante observa
transacciones en la mempool y envía otras con mayor prioridad para
ejecutarse antes. Este fenómeno forma parte del problema más amplio
del **MEV (Maximal Extractable Value)** y afecta especialmente a
aplicaciones DeFi. \[35\]

Otro riesgo importante es la **manipulación de oráculos**. Si un
contrato depende de precios externos que pueden alterarse temporalmente,
un atacante puede aprovechar esa situación para obtener beneficios
indebidos, por ejemplo, en protocolos de préstamo. \[33\]

En esta categoría también se incluyen los problemas de **aleatoriedad
insegura** y el uso de block.timestamp como fuente de decisiones
críticas. Estas variables no son completamente fiables ni impredecibles,
por lo que pueden ser manipuladas o anticipadas en determinados
escenarios.

### Errores lógicos de negocio

Los errores más difíciles de detectar son los relacionados con la lógica
del contrato.

En estos casos, el código puede ser correcto desde el punto de vista
técnico, pero implementar una lógica incorrecta. Esto incluye errores en
cálculos de balances, distribución de recompensas, gestión de estados o
validación de condiciones. \[31\]

Este tipo de vulnerabilidades es especialmente relevante porque suele
escapar a las herramientas automáticas. Además, muchos ataques reales
combinan errores lógicos con otros factores, como manipulación de
precios o condiciones de ejecución. \[35\]

### Conclusión

En conjunto, la seguridad en contratos inteligentes no puede abordarse
únicamente mediante la detección de patrones conocidos. Aunque
vulnerabilidades como reentrancy o overflow siguen siendo relevantes,
los problemas más complejos suelen estar relacionados con el diseño del
sistema, la interacción con otros componentes y la lógica de negocio.

Esto implica que una auditoría efectiva debe analizar no solo el código,
sino también su comportamiento, sus dependencias y los incentivos que lo
rodean.

## Ataques Reales

El estudio de incidentes reales constituye una fuente de conocimiento
imprescindible en el ámbito de la seguridad de contratos inteligentes. A
diferencia de los entornos de prueba, los ataques producidos en redes de
producción demuestran cómo las vulnerabilidades teóricas se traducen en
pérdidas económicas concretas e irreversibles.

En esta sección se analizan cuatro casos históricos representativos,
seleccionados por su relevancia técnica y su correspondencia directa con
cada una de las categorías de vulnerabilidades descritas en la sección
anterior (4.4. Vulnerabilidades de seguridad en contratos inteligentes
de Ethereum).

### Vulnerabilidad técnica de ejecución: The DAO (2016)

El ataque contra The DAO, producido en junio de 2016, representa el caso
más paradigmático de explotación de una vulnerabilidad de *reentrancy*
en la historia de Ethereum \[36\]. The DAO era un fondo de inversión
descentralizado desplegado sobre Ethereum que había recaudado
aproximadamente 150 millones de dólares en ETH procedentes de más de
once mil participantes, convirtiéndose en uno de los mayores proyectos
de financiación colectiva hasta ese momento \[37\].

La vulnerabilidad residía en la función withdraw() del contrato. El
flujo de ejecución enviaba los fondos en ETH al destinatario antes de
actualizar el balance interno correspondiente. Esta secuencia incorrecta
permitió a un atacante desplegar un contrato receptor cuya función de
*fallback* re-invocaba withdraw() de forma recursiva, extrayendo fondos
de manera repetida mientras el saldo del contrato permanecía sin
modificar. El ataque se ejecutó en múltiples iteraciones dentro de una
misma cadena de llamadas, drenando aproximadamente 3,6 millones de ETH
\[38\].

Las consecuencias del incidente trascendieron lo puramente económico. La
comunidad de Ethereum debatió durante semanas sobre cómo dar respuesta
al ataque, dado el carácter inmutable del protocolo. Finalmente, se
ejecutó un *hard fork* en el bloque 1.920.000, el 20 de julio de 2016,
que revirtió el estado de la cadena para recuperar los fondos. Una
fracción de la comunidad rechazó esta intervención por considerarla
contraria a los principios de inmutabilidad de la tecnología blockchain,
lo que dio lugar a la bifurcación conocida como Ethereum Classic \[37\].

Este caso puso de manifiesto que el patrón de diseño correcto para
gestionar transferencias es el denominado *checks-effects-interactions*:
primero verificar condiciones, después actualizar el estado del contrato
y, por último, realizar cualquier llamada externa. Su incumplimiento en
The DAO, a pesar de la aparente sencillez del principio, resultó en
pérdidas valoradas en torno a 60 millones de dólares al precio del
momento \[36\].

### Vulnerabilidad de control y privilegios: Poly Network (2021)

El ataque a Poly Network, ocurrido el 10 de agosto de 2021, ilustra con
especial claridad las consecuencias de un control de acceso deficiente
en contratos que gestionan operaciones críticas de alto valor \[39\].
Poly Network es un protocolo de interoperabilidad *cross-chain* que
conecta diversas redes blockchain, lo que amplía considerablemente su
superficie de ataque.

El vector de explotación se basó en una ausencia de restricciones en la
cadena de llamadas entre contratos del protocolo. La función
verifyHeaderAndExecuteTx(), presente en el contrato
EthCrossChainManager, permitía invocar internamente la función
PutCurEpochConPubKeyBytes() del contrato EthCrossChainData, encargada de
actualizar la clave pública del grupo de *keepers* con permisos para
ejecutar transacciones *cross-chain*. Al no existir ninguna comprobación
que restringiese qué direcciones podían realizar esta invocación de
forma indirecta, el atacante fue capaz de sustituir los *keepers*
legítimos por una dirección bajo su propio control.

La operación se replicó de forma simultánea en tres redes: Ethereum, BNB
Chain y Polygon; lo que supuso un control inmediato sobre la práctica
totalidad de los fondos bloqueados en el protocolo, con un valor
estimado de 611 millones de dólares, convirtiéndose en el mayor robo de
la historia del ecosistema DeFi hasta esa fecha.

El desenlace del incidente fue inusual: el atacante devolvió la
totalidad de los fondos en los días posteriores, argumentando haber
actuado con el propósito de demostrar la vulnerabilidad. No obstante, el
caso evidencia que errores de diseño en el modelo de permisos
(independientemente de su recuperabilidad) pueden comprometer
completamente la integridad de un protocolo. Una correcta implementación
de control de acceso, mediante modificadores de autorización explícitos
y separación de privilegios entre contratos, habría impedido la escalada
de permisos aprovechada en este ataque \[40\].

### Vulnerabilidad económica y dependencia del entorno: bZx (2020)

Los ataques contra el protocolo bZx, producidos en febrero de 2020,
constituyen uno de los primeros ejemplos documentados de explotación
combinada de *flash loans* y manipulación de oráculos de precio a escala
en el ecosistema DeFi. Su relevancia radica no solo en las pérdidas
económicas, sino en haber demostrado que la composabilidad de los
protocolos DeFi puede convertirse en un vector de ataque cuando los
componentes individuales no contemplan escenarios de manipulación
externa \[41\].

En el primero de los dos incidentes, acaecido el 14 de febrero de 2020,
el atacante obtuvo un préstamo flash de 10.000 ETH a través del
protocolo dYdX sin necesidad de aportar colateral alguno. Con una parte
de estos fondos abrió simultáneamente una posición corta apalancada
sobre el par WBTC/ETH en bZx y utilizó el volumen restante para adquirir
WBTC en Uniswap, manipulando artificialmente el precio de mercado del
par en ese pool. El protocolo bZx, al depender de Uniswap como fuente de
precios en tiempo real, calculó incorrectamente la valoración de la
posición del atacante, quien la cerró obteniendo un beneficio aproximado
de 350.000 dólares una vez devuelto el préstamo flash, todo dentro de
una única transacción \[42\].

El segundo ataque, cuatro días después, siguió una mecánica similar pero
orientada a la manipulación del precio del token sUSD en Kyber Network.
Al inflar artificialmente su cotización, el atacante logró depositar
colateral sobrevalorado en bZx y extraer en préstamo un volumen de
activos muy superior al que le habría correspondido según condiciones de
mercado normales \[42\].

Ambos ataques pusieron de manifiesto que la seguridad de un protocolo
DeFi no puede analizarse de forma aislada: la dependencia de precios
obtenidos de fuentes únicas y manipulables en tiempo real constituye una
vulnerabilidad estructural. La adopción de oráculos descentralizados con
agregación de múltiples fuentes de precio (como los proporcionados por
protocolos del tipo Chainlink) y el uso de precios promediados en el
tiempo (TWAP, *Time-Weighted Average Price*) son las principales
contramedidas frente a este patrón de ataque.

### Error lógico de negocio: Euler Finance (2023)

El ataque a Euler Finance, ejecutado el 13 de marzo de 2023, representa
un ejemplo de elevada complejidad técnica dentro de la categoría de
errores lógicos, precisamente porque la vulnerabilidad no residía en un
patrón de codificación inseguro clásico, sino en una interacción no
prevista entre mecanismos financieros del propio protocolo \[43\].

Euler Finance era un protocolo de préstamos descentralizado en Ethereum
que introducía el concepto de *sub-cuentas* para gestionar posiciones de
colateral y deuda de forma independiente. La vulnerabilidad se
encontraba en la función donateToReserves(), incorporada en una
actualización anterior. Esta función permitía a un usuario transferir
sus propios activos a las reservas del protocolo, pero no verificaba que
dicha operación no dejase la cuenta del donante en un estado de
insolvencia. En condiciones normales, esta situación habría sido
detectada por el sistema de liquidación, pero el atacante aprovechó el
mecanismo de autoliquidación del protocolo de una forma no contemplada
en su diseño \[44\].

El flujo del ataque comenzó con la obtención de un préstamo flash de 30
millones de DAI desde el protocolo Aave. Con estos fondos, el atacante
depositó colateral en Euler y, mediante operaciones de apalancamiento
repetidas, construyó posiciones de aproximadamente 195 millones de eDAI
(depósitos) y 200 millones de dDAI (deuda). A continuación, utilizó
donateToReserves() para crear intencionalmente una posición insolvente y
acto seguido activó la autoliquidación. El sistema de Euler, al calcular
el bonus de liquidación sobre una posición de ese tamaño, transfirió al
atacante los fondos de las reservas del protocolo en una cuantía muy
superior a la deuda original \[45\].

La pérdida total ascendió a aproximadamente 197 millones de dólares. Sin
embargo, el atacante devolvió la práctica totalidad de los fondos
semanas después, tras una negociación directa con el equipo de Euler
mediante mensajes publicados en la cadena de bloques. El incidente
ilustra cómo la ausencia de validaciones sobre invariantes de negocio
(en este caso, que ninguna operación debería permitir dejar una cuenta
en estado de insolvencia) puede generar vulnerabilidades que escapan
tanto a la revisión manual del código como a las herramientas de
análisis estático-convencionales \[44\].

## Síntesis y limitaciones del estado del arte

El análisis realizado muestra que el ecosistema de contratos
inteligentes compatibles con la Ethereum Virtual Machine (EVM) concentra
actualmente la mayor parte de herramientas, investigaciones y estándares
relacionados con la seguridad en blockchain. Solidity se ha consolidado
como el lenguaje dominante en el desarrollo de aplicaciones
descentralizadas y protocolos DeFi, lo que ha favorecido la aparición de
múltiples herramientas especializadas para el análisis de
vulnerabilidades.

No obstante, el estado del arte también evidencia limitaciones
relevantes. Herramientas como Slither, Mythril o Echidna utilizan
enfoques distintos y generan resultados heterogéneos, dificultando la
correlación de hallazgos y aumentando la necesidad de validación manual
por parte de auditores especializados. Asimismo, muchas soluciones
presentan dificultades para priorizar riesgos o contextualizar el
impacto real de las vulnerabilidades detectadas.

Por otro lado, gran parte de las vulnerabilidades analizadas dependen
principalmente del modelo de ejecución de la EVM y del diseño de los
contratos inteligentes, siendo extrapolables a distintas redes
compatibles como Ethereum, BNB Smart Chain, Polygon o Arbitrum. Por este
motivo, el presente trabajo utilizará BNB Smart Chain Testnet como
entorno de pruebas, aprovechando su compatibilidad con Solidity y la
reducción de costes durante el desarrollo experimental.

En conjunto, estas limitaciones justifican la necesidad de desarrollar
soluciones que permitan integrar múltiples herramientas de análisis,
normalizar resultados y facilitar una interpretación más estructurada de
los hallazgos de seguridad en contratos inteligentes.

# Objetivos concretos y metodología de trabajo

## Objetivo general

El objetivo general del presente Trabajo Fin de Máster consiste en
diseñar, implementar y evaluar una librería en Python orientada al
análisis de seguridad de contratos inteligentes compatibles con la
Ethereum Virtual Machine (EVM), capaz de integrar y correlacionar
resultados procedentes de distintas herramientas de auditoría.

La propuesta busca facilitar el análisis de vulnerabilidades en
contratos desarrollados en Solidity mediante un enfoque modular que
permita unificar resultados heterogéneos y mejorar la interpretación de
los hallazgos detectados.

## Objetivos específicos

Para alcanzar el objetivo general se plantean los siguientes objetivos
específicos:

- Analizar las principales vulnerabilidades de seguridad presentes en
  contratos inteligentes desarrollados en Solidity y las técnicas
  utilizadas para su detección.

- Estudiar el funcionamiento, capacidades y limitaciones de herramientas
  de análisis como Slither, Mythril y Echidna.

- Diseñar una arquitectura modular en Python que permita integrar
  distintas herramientas de análisis de contratos inteligentes.

- Implementar mecanismos de normalización y correlación de resultados
  para unificar hallazgos procedentes de diferentes herramientas.

- Desarrollar un sistema de generación de informes que facilite la
  interpretación de vulnerabilidades detectadas durante el análisis.

- Evaluar el funcionamiento de la librería utilizando contratos
  vulnerables conocidos y contratos reales de código abierto compatibles
  con la EVM.

## Metodología del trabajo

El desarrollo del trabajo se estructurará en varias fases orientadas
tanto al análisis teórico como a la implementación práctica de la
solución propuesta.

En una primera fase se realizará un estudio del estado del arte
relacionado con blockchain, contratos inteligentes, vulnerabilidades en
Solidity y técnicas de auditoría de seguridad. También se analizarán
distintas herramientas existentes para identificar sus capacidades,
limitaciones y posibilidades de integración.

Posteriormente, se definirá la arquitectura de la librería,
estableciendo los distintos módulos necesarios para la ejecución de
herramientas externas, el procesamiento de resultados y la generación de
informes. Durante esta fase se priorizará un diseño modular y extensible
que facilite futuras ampliaciones.

A continuación, se llevará a cabo la implementación de la solución
utilizando Python como lenguaje principal. La librería integrará
herramientas externas de análisis y permitirá procesar y correlacionar
sus resultados de forma automatizada.

Finalmente, se desarrollará una fase de evaluación experimental
utilizando contratos inteligentes vulnerables y casos reales obtenidos
de repositorios públicos. Los resultados obtenidos permitirán analizar
el comportamiento de la solución propuesta y validar su utilidad como
apoyo al análisis de seguridad de contratos inteligentes.

# Desarrollo específico de la contribución

## Identificación de requisitos

El desarrollo de la librería evmaudit parte de un conjunto de requisitos
funcionales y no funcionales derivados directamente de las limitaciones
identificadas en el estado del arte y de los objetivos específicos
definidos en el capítulo anterior.

Desde el punto de vista funcional, el sistema debe ser capaz de ejecutar
las herramientas de análisis Slither, Mythril y Echidna sobre contratos
inteligentes en formato de código fuente Solidity, recopilar sus
resultados crudos y procesarlos de forma automatizada. Asimismo, debe
transformar dichos resultados a un esquema de datos común que permita
operar sobre ellos de forma uniforme con independencia de la herramienta
que los haya generado. El sistema debe detectar hallazgos duplicados o
relacionados reportados por múltiples herramientas, consolidarlos en
grupos coherentes y asignarles una puntuación de confianza basada en el
grado de confirmación cruzada. Finalmente, debe presentar los hallazgos
ordenados por severidad y exportar el resultado en formatos
estructurados adecuados tanto para consumo humano como para integración
en pipelines automatizados.

Desde el punto de vista no funcional, se priorizan la modularidad y la
extensibilidad, de forma que sea posible incorporar nuevas herramientas
de análisis o nuevos formatos de salida sin modificar el núcleo del
sistema. La librería debe ejecutarse íntegramente en entornos locales
sin dependencias de servicios externos de pago, estar implementada en
Python y ser compatible con contratos desarrollados para redes EVM,
incluyendo Ethereum mainnet y BNB Smart Chain Testnet como entorno de
pruebas principal.

## Descripción de la herramienta software desarrollada

La librería evmaudit se organiza en torno a una arquitectura de pipeline
en capas, en la que cada capa recibe como entrada la salida de la capa
anterior y produce un resultado más elaborado y estructurado. Este
diseño facilita la separación de responsabilidades, simplifica las
pruebas unitarias de cada componente y permite sustituir o ampliar
módulos individuales sin afectar al resto del sistema.

El flujo de procesamiento completo puede representarse de la siguiente
forma:

![[]{#_Toc230713173 .anchor}Figura 2. *Pipeline
EVMAudit*](media/image3.png){width="2.2058038057742784in"
height="5.963636264216973in"}

El paquete se estructura en cinco módulos principales que implementan
cada una de las fases del pipeline:

- **evmaudit.runner:** ejecución de las herramientas externas y
  recopilación de salidas crudas.

- **evmaudit.normalizer:** transformación de cada salida cruda al
  esquema de datos común Finding.

- **evmaudit.correlator:** agrupación, deduplicación y scoring de
  hallazgos cruzados.

- **evmaudit.prioritizer:** ordenación y clasificación por categoría de
  vulnerabilidad.

**evmaudit.reporter:** generación de informes en múltiples formatos.

### Módulo 1: Ejecución de herramientas (evmaudit.runner)

Este módulo constituye el punto de entrada del pipeline. Su
responsabilidad es lanzar las herramientas de análisis externas sobre el
contrato objetivo y recopilar sus salidas en formato JSON sin ningún
tipo de procesamiento adicional. De este modo, el módulo actúa como una
capa de integración que desacopla el resto del sistema de los detalles
de invocación de cada herramienta, facilitando futuras incorporaciones
de nuevas herramientas sin modificar las capas superiores.

Cada función de este módulo invoca la herramienta correspondiente como
subproceso del sistema operativo, captura su salida estándar y de error,
gestiona los posibles códigos de retorno anómalos (por ejemplo, timeouts
en Mythril o errores de compilación en Slither) y devuelve un
diccionario Python con los resultados crudos listos para ser procesados
por el módulo de normalización.

Las funciones implementadas en este módulo son las siguientes:

**run_slither(contract_path: str, config: dict = None) → dict**

Ejecuta Slither sobre el archivo Solidity especificado en contract_path
y devuelve su salida en formato JSON. Slither se invoca con la opción
\--json - para obtener la salida estructurada por la salida estándar,
evitando así la generación de archivos intermedios. El parámetro config
permite especificar opciones adicionales de ejecución, como el
subconjunto de detectores a activar, la versión del compilador Solidity
(solc) o la ruta a un archivo de configuración YAML propio de Slither.
En caso de que Slither no detecte ninguna vulnerabilidad, la función
devuelve igualmente un diccionario con estructura válida y lista de
hallazgos vacía, evitando que el pipeline se interrumpa por ausencia de
resultados.

resultado = run_slither(\"contratos/VulnerableBank.sol\")

\# Devuelve:

{

\"success\": true,

\"tool\": \"slither\",

\"raw\": { \... } \# Salida JSON completa de Slither

}

**run_mythril(contract_path: str, timeout: int = 120, depth: int = 22) →
dict**

Ejecuta Mythril en modo de análisis de seguridad (analyze) sobre el
contrato especificado. Los parámetros timeout y depth permiten controlar
respectivamente el tiempo máximo de ejecución y la profundidad de
exploración del grafo de estados simbólicos, dos variables críticas para
gestionar el problema de explosión de caminos (*path explosion*)
descrito en el estado del arte. El valor por defecto de depth=22 es el
recomendado por la documentación oficial de Mythril para contratos de
complejidad media. La función detecta automáticamente si la herramienta
ha terminado por timeout y lo indica en el campo status del resultado
devuelto, de forma que las capas posteriores puedan ponderar
adecuadamente la confianza de los hallazgos obtenidos bajo análisis
incompleto.

resultado = run_mythril(\"contratos/VulnerableBank.sol\", timeout=60,
depth=10)

\# Devuelve:

{

\"success\": true,

\"tool\": \"mythril\",

\"status\": \"complete\", \# O \"timeout\" si se agotó el tiempo

\"raw\": { \... } \# Salida JSON completa de Mythril

}

**\**

**run_echidna(contract_path: str, config_path: str = None) → dict**

Ejecuta Echidna sobre el contrato especificado en modo de fuzzing basado
en propiedades. El parámetro opcional config_path permite proporcionar
un archivo de configuración YAML con parámetros de la campaña de
fuzzing, como el número de transacciones a generar, la semilla aleatoria
o el nombre del contrato a analizar. Si no se proporciona configuración,
la función aplica una configuración por defecto razonable para análisis
de propósito general. Dado que Echidna requiere que las propiedades a
verificar estén definidas como funciones con el prefijo echidna\_ dentro
del propio contrato, esta función es especialmente útil cuando los
contratos bajo análisis ya incorporan este tipo de aserciones, siendo
complementaria a Slither y Mythril en contratos que no las incluyan.

resultado = run_echidna(\"contratos/VulnerableBank.sol\")

\# Devuelve:

{

\"success\": true,

\"tool\": \"echidna\",

\"raw\": { \... } \# Salida JSON completa de Echidna

}

La salida agregada de las tres funciones anteriores constituye el objeto
de entrada de la capa de normalización y tiene la siguiente estructura:

{

\"slither\": { \"success\": true, \"tool\": \"slither\", \"raw\": { \...
} },

\"mythril\": { \"success\": true, \"tool\": \"mythril\", \"status\":
\"complete\", \"raw\": { \... } },

\"echidna\": { \"success\": true, \"tool\": \"echidna\", \"raw\": { \...
} }

}

### Módulo 2: Normalización (evmaudit.normalizer)

Este módulo implementa la primera capa de transformación del pipeline.
Su objetivo es convertir las salidas heterogéneas de Slither, Mythril y
Echidna en una lista uniforme de objetos Finding, eliminando las
diferencias de formato, nomenclatura y nivel de detalle que caracterizan
a cada herramienta y que, tal como se describe en el estado del arte,
constituyen uno de los principales obstáculos para la correlación
automatizada de resultados.

El modelo de datos común Finding es una clase de datos Python
(dataclass) con los siguientes campos obligatorios:

- tool: nombre de la herramienta que generó el hallazgo (\"slither\",
  \"mythril\" o \"echidna\").

- title: descripción breve del tipo de vulnerabilidad detectada.

- description: descripción detallada del hallazgo, incluyendo el
  contexto de ejecución cuando esté disponible.

- severity: nivel de severidad normalizado al esquema común
  (\"critical\", \"high\", \"medium\", \"low\", \"informational\").

- category: categoría de vulnerabilidad según la clasificación utilizada
  en el estado del arte (\"execution\", \"access_control\",
  \"economic\", \"business_logic\").

- location: diccionario con los campos file y line, indicando la
  ubicación exacta del hallazgo en el código fuente.

- swc_id: identificador del estándar Smart Contract Weakness
  Classification (SWC), cuando la herramienta lo proporciona o puede
  inferirse del tipo de detector.

- raw: datos adicionales específicos de la herramienta, preservados
  íntegramente para consulta posterior.

Las funciones implementadas en este módulo son las siguientes:

**normalize_slither_output(raw_output: dict) → list\[Finding\]**

Procesa la salida JSON de Slither y extrae los hallazgos relevantes. La
salida de Slither organiza los resultados en una lista de detectores
activados, cada uno con campos como check (nombre del detector), impact
(severidad declarada), confidence, description y una lista de elementos
(elements) que identifican las ubicaciones del código afectadas. Esta
función itera sobre dicha lista, mapea el campo impact al esquema de
severidad común (traduciendo, por ejemplo, \"High\" a \"high\"), asigna
la categoría de vulnerabilidad correspondiente a partir de una tabla de
correspondencia entre nombres de detectores de Slither y las categorías
definidas en el trabajo, e infiere el identificador SWC cuando existe un
mapeo establecido por la comunidad. En casos donde un mismo detector de
Slither reporte múltiples ubicaciones afectadas, la función genera un
objeto Finding independiente por cada ubicación, facilitando su
posterior correlación línea a línea.

**normalize_mythril_output(raw_output: dict) → list\[Finding\]**

Procesa la salida JSON de Mythril, cuya estructura difiere
significativamente de la de Slither. Mythril organiza sus resultados
como una lista de issues, cada uno con campos como swc-id, title,
description, severity, lineno y opcionalmente una secuencia de
transacciones (tx_sequence) que permite reproducir el exploit. Esta
función extrae directamente el swc_id cuando está disponible, mapea la
severidad al esquema común y construye la ubicación del hallazgo a
partir del campo lineno. La presencia de la traza de transacciones se
incorpora al campo raw del objeto Finding para que pueda ser consultada
en el informe final.

**normalize_echidna_output(raw_output: dict) → list\[Finding\]**

Procesa la salida de Echidna, que reporta las propiedades falsadas
durante la campaña de fuzzing junto con la secuencia mínima de
transacciones que produce la violación. Dado que Echidna no asigna
identificadores SWC ni categorías de vulnerabilidad de forma explícita,
esta función infiere la categoría a partir del nombre de la propiedad
violada cuando sigue la convención de nomenclatura estándar
(echidna_no_reentrancy, echidna_balance_invariant, etc.), y asigna una
severidad por defecto de \"high\" dado que cualquier violación de
propiedad representa un comportamiento inesperado confirmado mediante
ejecución real del contrato. La secuencia de llamadas que produce la
violación se preserva en el campo raw.

La salida de este módulo es una lista consolidada de objetos Finding de
todas las herramientas, con la siguiente representación JSON:

{

\"findings\": \[

{

\"tool\": \"slither\",

\"title\": \"Reentrancy vulnerability\",

\"description\": \"La función withdraw() realiza una llamada externa
antes de actualizar el balance interno\...\",

\"severity\": \"high\",

\"category\": \"execution\",

\"location\": { \"file\": \"VulnerableBank.sol\", \"line\": 18 },

\"swc_id\": \"SWC-107\",

\"raw\": { \... }

},

{

\"tool\": \"mythril\",

\"title\": \"External Call To User-Supplied Address\",

\"description\": \"Se detecta una llamada externa en un estado en el que
el balance no ha sido actualizado\...\",

\"severity\": \"high\",

\"category\": \"execution\",

\"location\": { \"file\": \"VulnerableBank.sol\", \"line\": 18 },

\"swc_id\": \"SWC-107\",

\"raw\": { \... }

}

\]

}

### Módulo 3: Correlación (evmaudit.correlator)

Este módulo implementa la segunda capa del pipeline y constituye la
contribución técnica central de la librería. Su objetivo es identificar
qué hallazgos de distintas herramientas se refieren a la misma
vulnerabilidad concreta en el código, agruparlos en un único objeto
correlacionado y asignarle una puntuación de confianza proporcional al
grado de confirmación cruzada obtenido. Este proceso aborda directamente
los problemas de detección redundante y de elevada tasa de falsos
positivos identificados como limitaciones del estado del arte.

El principio de funcionamiento del módulo se basa en la hipótesis de que
si dos o más herramientas con técnicas de análisis complementarias
(análisis estático, ejecución simbólica y fuzzing) coinciden en señalar
el mismo tipo de vulnerabilidad en la misma región del código, la
probabilidad de que el hallazgo sea un verdadero positivo aumenta
significativamente. Esta hipótesis está respaldada por los resultados
del estudio empírico de Durieux et al. \[26\], que demuestra que la tasa
de falsos positivos de herramientas individuales como Mythril puede
alcanzar el 52%, mientras que la confirmación cruzada entre herramientas
reduce considerablemente dicha tasa.

Las funciones implementadas en este módulo son las siguientes:

**deduplicate_findings(findings: list\[Finding\]) →
list\[FindingGroup\]**

Recibe la lista de hallazgos normalizados producida por el módulo
anterior e identifica aquellos que se refieren a la misma
vulnerabilidad. El criterio de agrupación combina dos dimensiones: el
tipo de vulnerabilidad (campo swc_id cuando está disponible, o category
en su defecto) y la proximidad de la ubicación en el código fuente
(campo location.line). Dos hallazgos se consideran duplicados si
comparten el mismo swc_id y sus líneas de código se encuentran dentro de
un margen de tolerancia configurable (por defecto, ±3 líneas), margen
que compensa las diferencias menores en la identificación de líneas
entre herramientas que operan sobre el AST (Slither) frente a las que
operan sobre el bytecode (Mythril).

El resultado es una lista de objetos FindingGroup, cada uno de los
cuales agrega todos los hallazgos individuales correspondientes a la
misma vulnerabilidad detectada, independientemente de la herramienta que
los haya generado.

**assign_confidence_score(group: FindingGroup) → FindingGroup**

Calcula y asigna la puntuación de confianza (confidence_score) a cada
grupo de hallazgos correlacionados. La puntuación se calcula en función
del número de herramientas distintas que han confirmado la
vulnerabilidad:

Un hallazgo confirmado únicamente por una herramienta recibe una
puntuación de 1, lo que indica baja confianza y mayor probabilidad de
ser un falso positivo.

Si dos herramientas lo han confirmado, la puntuación asciende a 2,
indicando confianza moderada.

Si las tres herramientas coinciden, la puntuación alcanza su valor
máximo de 3, indicando alta confianza en la existencia real de la
vulnerabilidad.

Adicionalmente, la función pondera la combinación de herramientas que
confirman el hallazgo: la coincidencia entre Slither (análisis estático)
y Mythril (ejecución simbólica) se considera especialmente significativa
al tratarse de técnicas complementarias que operan a distintos niveles
de abstracción. La puntuación final puede extenderse en el futuro para
incorporar factores adicionales como la severidad declarada o la
especificidad del detector activado.

**correlate_findings(findings: list\[Finding\]) → list\[FindingGroup\]**

Función orquestadora que combina internamente deduplicate_findings y
assign_confidence_score, devolviendo directamente la lista de grupos
correlacionados con sus puntuaciones de confianza asignadas. Es la
función principal de este módulo en el uso típico de la librería.

La salida del módulo de correlación tiene la siguiente estructura JSON:

{

\"contract\": \"VulnerableBank\",

\"findings\": \[

{

\"swc_id\": \"SWC-107\",

\"vuln_type\": \"reentrancy\",

\"severity\": \"high\",

\"confidence_score\": 2,

\"status\": \"confirmed\",

\"lines\": \[15, 18\],

\"confirmed_by\": \[\"slither\", \"mythril\"\],

\"evidence\": {

\"slither\": { \"check\": \"reentrancy-eth\", \"impact\": \"High\" },

\"mythril\": { \"lineno\": 18, \"tx_sequence\": { \... } }

}

}

\]

}

El campo status puede tomar los valores \"confirmed\" (dos o más
herramientas), \"potential\" (una única herramienta) o
\"low_confidence\" (cuando la herramienta que lo reporta tiene una tasa
de falsos positivos históricamente elevada para ese tipo de detector
concreto, según la tabla de referencia incorporada en el módulo).

### Módulo 4: Priorización (evmaudit.prioritizer)

Este módulo implementa la tercera capa del pipeline y tiene como
objetivo ordenar los hallazgos correlacionados de mayor a menor
relevancia para el auditor, facilitando que los riesgos más críticos
sean atendidos en primer lugar. Para ello, combina dos dimensiones de
evaluación: la severidad intrínseca de la vulnerabilidad y la confianza
en que el hallazgo es un verdadero positivo.

Las funciones implementadas en este módulo son las siguientes:

**calculate_severity_score(group: FindingGroup) → float**

Calcula una puntuación numérica de severidad combinada para cada grupo
de hallazgos correlacionados. La puntuación se obtiene a partir de dos
factores. El primero es la severidad normalizada del hallazgo,
codificada numéricamente como critical=4, high=3, medium=2, low=1 e
informational=0. El segundo es la puntuación de confianza asignada por
el módulo de correlación, normalizada al rango \[0, 1\] dividiéndola
entre el valor máximo posible (3). La puntuación combinada se calcula
como el producto de ambos factores, lo que produce una escala continua
en el rango \[0, 4\] que pondera conjuntamente la gravedad potencial y
la fiabilidad del hallazgo. Un hallazgo crítico confirmado por tres
herramientas obtendrá la puntuación máxima de 4.0, mientras que un
hallazgo de severidad media reportado por una sola herramienta obtendrá
una puntuación de aproximadamente 0.67, reflejando la incertidumbre
asociada.

**rank_findings(groups: list\[FindingGroup\]) → list\[FindingGroup\]**

Ordena la lista de grupos de hallazgos de mayor a menor puntuación de
severidad combinada. En caso de empate en la puntuación, los hallazgos
se ordenan secundariamente por el número de herramientas que los han
confirmado y, en tercer lugar, alfabéticamente por el identificador SWC
para garantizar un orden determinista en la salida. El resultado es una
lista ordenada que permite al auditor abordar los hallazgos en el orden
de prioridad más adecuado.

**classify_by_category(groups: list\[FindingGroup\]) → dict\[str,
list\[FindingGroup\]\]**

Organiza los hallazgos en un diccionario indexado por las cuatro
categorías de vulnerabilidad definidas en el estado del arte:
\"execution\" para vulnerabilidades técnicas de ejecución (reentrancy,
overflow, delegatecall inseguro, DoS), \"access_control\" para problemas
de control y privilegios (funciones sin restricciones, uso de tx.origin,
inicialización insegura), \"economic\" para vulnerabilidades económicas
y de dependencia del entorno (front-running, manipulación de oráculos,
block.timestamp) y \"business_logic\" para errores lógicos de negocio
(cálculos incorrectos de balances, distribución de recompensas, estados
inconsistentes). Esta clasificación facilita el análisis estructurado
por parte del auditor y permite generar secciones temáticas en el
informe final.

### Módulo 5: Generación de informes (evmaudit.reporter)

Este módulo constituye la capa de salida del pipeline y se encarga de
transformar los hallazgos priorizados en informes consumibles. Su diseño
tiene en cuenta dos perfiles de uso diferenciados: por un lado,
auditores de seguridad que necesitan un documento estructurado y legible
con contexto suficiente para validar y remediar cada hallazgo; por otro,
sistemas automatizados de CI/CD que consumen los resultados como datos
estructurados para integrarse en flujos de revisión de código.

Las funciones implementadas en este módulo son las siguientes:

**generate_summary(groups: list\[FindingGroup\]) → dict**

Produce un resumen ejecutivo en forma de diccionario Python con los
siguientes campos: número total de hallazgos, desglose por severidad
(critical, high, medium, low, informational), desglose por categoría de
vulnerabilidad, desglose por herramienta origen y una puntuación global
de riesgo del contrato calculada como la media ponderada de las
puntuaciones de severidad combinada de todos los hallazgos, expresada en
una escala de 0 a 100. Este resumen está concebido para proporcionar una
visión inmediata del estado de seguridad del contrato antes de descender
al detalle de cada hallazgo individual.

{

\"total_findings\": 5,

\"by_severity\": { \"critical\": 0, \"high\": 2, \"medium\": 2, \"low\":
1, \"informational\": 0 },

\"by_category\": { \"execution\": 2, \"access_control\": 1,
\"economic\": 1, \"business_logic\": 1 },

\"by_tool\": { \"slither\": 4, \"mythril\": 3, \"echidna\": 1 },

\"risk_score\": 68.4

}

**generate_report(groups: list\[FindingGroup\], format: str = \"json\",
output_path: str = None) → str**

Genera el informe completo de auditoría a partir de los hallazgos
priorizados. El parámetro format controla el formato de salida: \"json\"
produce un objeto JSON estructurado con todos los grupos de hallazgos y
su metadatos completos; \"markdown\" produce un documento Markdown con
secciones por categoría de vulnerabilidad, tablas de hallazgos ordenados
por prioridad y bloques de código que ilustran la ubicación de cada
vulnerabilidad; \"csv\" produce un archivo de valores separados por
comas adecuado para su importación en hojas de cálculo o herramientas de
gestión de vulnerabilidades. Si se proporciona output_path, el informe
se escribe en disco en la ruta indicada; en caso contrario, se devuelve
como cadena de texto. El informe en formato Markdown incluye, para cada
hallazgo, una descripción de la vulnerabilidad, la evidencia aportada
por cada herramienta confirmante, la ubicación exacta en el código y una
recomendación de mitigación basada en las mejores prácticas descritas en
el Anexo A del presente trabajo.

**export_to_sarif(groups: list\[FindingGroup\], output_path: str) →
None**

Exporta los hallazgos al formato estándar SARIF 2.1.0 (*Static Analysis
Results Interchange Format*), especificación abierta mantenida por OASIS
que es reconocida de forma nativa por plataformas de revisión de código
como GitHub Code Scanning y Azure DevOps. Este formato permite presentar
los hallazgos directamente en la interfaz de revisión de código de los
repositorios, anotando las líneas afectadas con los problemas
detectados. Su inclusión en la librería responde al objetivo de
facilitar la integración de evmaudit en flujos de trabajo de DevSecOps,
posibilitando el análisis automático de contratos en cada *pull request*
antes de su despliegue.

### Identificación de requisitos

### Descripción de la herramienta software desarrollada

### Evaluación

# Conclusiones y trabajo futuro

## Conclusiones

## Trabajo futuro

# Referencias bibliográficas {#referencias-bibliográficas .Título-1-sin-numerar}

\[1\] S. Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System."
\[Online\]. Available: www.bitcoin.org

\[2\] D. Yaga, P. Mell, N. Roby, and K. Scarfone, "Blockchain Technology
Overview," Jun. 2019, doi: 10.6028/NIST.IR.8202.

\[3\] L. Lamport, R. Shostak, and M. Pease, "The Byzantine Generals
Problem," 1982.

\[4\] L. Lamport, "Paxos Made Simple," 2001.

\[5\] T. Nakai, A. Sakurai, S. Hironaka, and K. Shudo, "The Blockchain
Trilemma Described by a Formula," in *Proceedings - 2023 IEEE
International Conference on Blockchain, Blockchain 2023*, Institute of
Electrical and Electronics Engineers Inc., 2023, pp. 41--46. doi:
10.1109/Blockchain60715.2023.00016.

\[6\] "¿Qué es el trilema de la blockchain?" Accessed: Apr. 14, 2026.
\[Online\]. Available:
https://www.binance.com/es/academy/articles/what-is-the-blockchain-trilemma

\[7\] N. Szabo, "Smart Contracts." Accessed: Apr. 13, 2026. \[Online\].
Available:
https://www.fon.hum.uva.nl/rob/Courses/InformationInSpeech/CDROM/Literature/LOTwinterschool2006/szabo.best.vwh.net/smart.contracts.html

\[8\] "Ethereum Smart Contract Best Practices." Accessed: Apr. 12, 2026.
\[Online\]. Available:
https://consensysdiligence.github.io/smart-contract-best-practices/

\[9\] DR. GAVIN WOOD, "ETHEREUM: A SECURE DECENTRALISED GENERALISED
TRANSACTION LEDGER," 2025. Accessed: Apr. 12, 2026. \[Online\].
Available: https://ethereum.github.io/yellowpaper/paper.pdf

\[10\] "Chapter 9: Smart Contract Security - Mastering Ethereum."
Accessed: Apr. 15, 2026. \[Online\]. Available:
https://masteringethereum.xyz/chapter_9.html

\[11\] "The Architecture of a Web 3.0 application." Accessed: Apr. 14,
2026. \[Online\]. Available:
https://www.preethikasireddy.com/post/the-architecture-of-a-web-3-0-application

\[12\] M. Saad *et al.*, "Exploring the Attack Surface of Blockchain: A
Systematic Overview".

\[13\] K. Qin, L. Zhou, B. Livshits, and A. Gervais, "Attacking the DeFi
Ecosystem with Flash Loans for Fun and Profit," 2021, pp. 3--32. doi:
10.1007/978-3-662-64322-8_1.

\[14\] L. Zhou *et al.*, "SoK: Decentralized Finance (DeFi) Attacks,"
Apr. 2023, \[Online\]. Available: http://arxiv.org/abs/2208.13035

\[15\] A. Zamyatin *et al.*, "SoK: Communication Across Distributed
Ledgers."

\[16\] R. Belchior, A. Vasconcelos, S. Guerreiro, and M. Correia, "A
Survey on Blockchain Interoperability: Past, Present, and Future
Trends," Nov. 30, 2022, *Association for Computing Machinery*. doi:
10.1145/3471140.

\[17\] H. Chu, P. Zhang, H. Dong, Y. Xiao, S. Ji, and W. Li, "A survey
on smart contract vulnerabilities: Data sources, detection and repair,"
*Inf. Softw. Technol.*, vol. 159, p. 107221, Jul. 2023, doi:
10.1016/j.infsof.2023.107221.

\[18\] J. Feist, G. Grieco, and A. Groce, "Slither: A Static Analysis
Framework For Smart Contracts," *Proceedings - 2019 IEEE/ACM 2nd
International Workshop on Emerging Trends in Software Engineering for
Blockchain, WETSEB 2019*, pp. 8--15, Aug. 2019, doi:
10.1109/WETSEB.2019.00008.

\[19\] "crytic/slither: Static Analyzer for Solidity and Vyper."
Accessed: Apr. 14, 2026. \[Online\]. Available:
https://github.com/crytic/slither

\[20\] "Smart Contract Security Newsletter #35 \| by Shayan Eskandari \|
Consensys Diligence \| Medium." Accessed: Apr. 14, 2026. \[Online\].
Available:
https://medium.com/consensys-diligence/smart-contract-security-newsletter-35-6411b3d0552b

\[21\] S. AL Amri, L. Aniello, and V. Sassone, "A Review of Upgradeable
Smart Contract Patterns based on OpenZeppelin Technique," *The Journal
of The British Blockchain Association*, vol. 6, no. 1, pp. 1--8, Apr.
2023, doi: 10.31585/jbba-6-1-(3)2023.

\[22\] "Slither - Building Secure Contracts." Accessed: Apr. 14, 2026.
\[Online\]. Available:
https://secure-contracts.com/program-analysis/slither/docs/src/

\[23\] "ConsenSysDiligence/mythril: Mythril is a
symbolic-execution-based securty analysis tool for EVM bytecode. It
detects security vulnerabilities in smart contracts built for Ethereum
and other EVM-compatible blockchains." Accessed: Apr. 14, 2026.
\[Online\]. Available: https://github.com/ConsenSysDiligence/mythril

\[24\] B. Mueller, "File 1 of 1 HITB SECCONF Amsterd4m and ConsenSys
Dilig3nce bring you
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Smashing
Ethereum Smart Contracts for Fun and Real Profit
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX," 2018.

\[25\] "🛡️ Smart Contract Security Wars: The Ultimate Slither vs Mythril
Battle Guide That Saves Your Protocol From Million-Dollar Hacks \| by
PMartin \| CoinsBench." Accessed: Apr. 14, 2026. \[Online\]. Available:
https://coinsbench.com/%EF%B8%8F-smart-contract-security-wars-the-ultimate-slither-vs-mythril-battle-guide-that-saves-your-837d67c49121

\[26\] T. Durieux, J. F. Ferreira, R. Abreu, and P. Cruz, "Empirical
Review of Automated Analysis Tools on 47,587 Ethereum Smart Contracts,"
*Proceedings - International Conference on Software Engineering*, pp.
530--541, Feb. 2020, doi: 10.1145/3377811.3380364.

\[27\] G. Grieco, W. Song, A. Cygan, J. Feist, and A. Groce, "Echidna:
Effective, usable, and fast fuzzing for smart contracts," *ISSTA 2020 -
Proceedings of the 29th ACM SIGSOFT International Symposium on Software
Testing and Analysis*, pp. 557--560, Jul. 2020, doi:
10.1145/3395363.3404366.

\[28\] "crytic/echidna: Ethereum smart contract fuzzer." Accessed: Apr.
15, 2026. \[Online\]. Available: https://github.com/crytic/echidna

\[29\] "How to use Echidna to test smart contracts \| ethereum.org."
Accessed: Apr. 15, 2026. \[Online\]. Available:
https://ethereum.org/developers/tutorials/how-to-use-echidna-to-test-smart-contracts/

\[30\] "Security Considerations --- Solidity 0.8.35-develop
documentation." Accessed: Apr. 14, 2026. \[Online\]. Available:
https://docs.soliditylang.org/en/latest/security-considerations.html?utm_source=chatgpt.com

\[31\] N. Atzei, M. Bartoletti, and T. Cimoli, "A survey of attacks on
Ethereum smart contracts (SoK)," Lecture Notes in Computer Science
(including subseries Lecture Notes in Artificial Intelligence and
Lecture Notes in Bioinformatics), vol. 10204 LNCS, pp. 164--186, 2017,
doi: 10.1007/978-3-662-54455-6_8/FIGURES/1.

\[32\] L. Brent *et al.*, "Vandal: A Scalable Security Analysis
Framework for Smart Contracts," Sep. 2018, \[Online\]. Available:
http://arxiv.org/abs/1809.03981

\[33\] Jinson Varghese Behanan and Shashank, "OWASP Smart Contract Top
10 \| OWASP Foundation." Accessed: Apr. 12, 2026. \[Online\]. Available:
https://owasp.org/www-project-smart-contract-top-10/

\[34\] "EEA EthTrust Security Levels Specification v-after-2 Editor's
Draft." Accessed: Apr. 12, 2026. \[Online\]. Available:
https://entethalliance.org/specs/ethtrust-sl/#sec-introduction

\[35\] C. Ferreira Torres, A. K. Iannillo, A. Gervais, and R. State,
"The Eye of Horus: Spotting and Analyzing Attacks on Ethereum Smart
Contracts".

\[36\] "Reentrancy Attacks and The DAO Hack Explained \| Chainlink."
Accessed: Apr. 15, 2026. \[Online\]. Available:
https://blog.chain.link/reentrancy-attacks-and-the-dao-hack/

\[37\] "CoinDesk Turns 10: 2016 - How The DAO Hack Changed Ethereum and
Crypto." Accessed: Apr. 15, 2026. \[Online\]. Available:
https://www.coindesk.com/consensus-magazine/2023/05/09/coindesk-turns-10-how-the-dao-hack-changed-ethereum-and-crypto

\[38\] "Ethereum DAO Hack." Accessed: Apr. 15, 2026. \[Online\].
Available: https://www.bitstamp.net/learn/crypto-101/ethereum-dao-hack/

\[39\] "The Poly Network Hack Explained - Kudelski Security Research
Center." Accessed: Apr. 15, 2026. \[Online\]. Available:
https://kudelskisecurity.com/research/the-poly-network-hack-explained

\[40\] R. Zhang, "Analysis and Research on Blockchain Security
Technology: A Case Study of the Poly Network Security Incident",
Accessed: Apr. 15, 2026. \[Online\]. Available:
http://www.stemmpress.com

\[41\] S. Jiang, W. You, S. Xuan, and J. Shen, "Decentralized finance
security: A survey of attacks, defenses, and open challenges,"
*High-Confidence Computing*, vol. 6, p. 100383, 2026, doi:
10.1016/j.hcc.2026.100383.

\[42\] "bZx Hack Full Disclosure (With Detailed Profit Analysis) \| by
PeckShield \| Medium." Accessed: Apr. 15, 2026. \[Online\]. Available:
https://peckshield.medium.com/bzx-hack-full-disclosure-with-detailed-profit-analysis-e6b1fa9b18fc

\[43\] H. Rezaei, M. Eshghie, K. Anderesson, and F. Palmieri, "SoK: Root
Cause of \$1 Billion Loss in Smart Contract Real-World Attacks via a
Systematic Literature Review of Vulnerabilities," Sep. 2025, doi:
10.14722/ndss.2025.\[23\|24\]xxxx.

\[44\] "Deep Dive Exploit Analysis: Euler Finance." Accessed: Apr. 15,
2026. \[Online\]. Available:
https://www.cyfrin.io/blog/how-did-the-euler-finance-hack-happen-hack-analysis

\[45\] "Euler Finance Flash Loan Attack Explained." Accessed: Apr. 15,
2026. \[Online\]. Available:
https://www.chainalysis.com/blog/euler-finance-flash-loan-attack/

 

# Ejemplos de vulnerabilidades en contratos inteligentes {#ejemplos-de-vulnerabilidades-en-contratos-inteligentes .Anexo}

Este anexo presenta ejemplos simplificados de vulnerabilidades
representativas en contratos inteligentes desarrollados en Solidity. El
objetivo es ilustrar de forma práctica los principales tipos de
debilidades descritas en la sección 4.4, facilitando su comprensión y su
posterior detección mediante herramientas automáticas.

Cada ejemplo incluye: descripción, fragmento de código vulnerable,
impacto y estrategia de mitigación.

A.1. Vulnerabilidades técnicas de ejecución

A.1.1. Reentrancy

La vulnerabilidad de
[**reentrancy**](https://www.cyfrin.io/blog/what-is-a-reentrancy-attack-solidity-smart-contracts)
se produce cuando un contrato realiza una llamada externa antes de
actualizar su estado interno, permitiendo que el contrato receptor
reingrese en la función original en un estado inconsistente.

Código vulnerable

contract VulnerableBank {

mapping(address =\> uint256) public balances;

function deposit() public payable {

balances\[msg.sender\] += msg.value;

}

function withdraw(uint256 amount) public {

require(balances\[msg.sender\] \>= amount);

(bool success, ) = msg.sender.call{value: amount}(\"\");

require(success);

balances\[msg.sender\] -= amount;

}

}

- **Impacto**: Un atacante puede drenar fondos repitiendo la llamada
  antes de que el balance sea actualizado.

- Mitigación:

  - Patrón
    [*Checks-Effects-Interactions*](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)

  - Uso de ReentrancyGuard

  - Actualizar el estado antes de llamadas externas

A.1.2. Integer Overflow / Underflow

Errores aritméticos que provocan desbordamientos en operaciones enteras.
Aunque mitigados en Solidity ≥0.8, siguen siendo relevantes en bloques
unchecked.

Código vulnerable

function increment(uint256 x) public pure returns (uint256) {

unchecked {

return x + 1;

}

}

- **Impacto**: Puede alterar balances o condiciones lógicas críticas.

- Mitigación:

  - Evitar unchecked salvo casos justificados

  - Uso de validaciones explícitas

A.1.3. Uso inseguro de delegatecall

La función delegatecall ejecuta código externo en el contexto de
almacenamiento del contrato llamador.

Código vulnerable

contract Proxy {

address public implementation;

function execute(bytes memory data) public {

(bool success, ) = implementation.delegatecall(data);

require(success);

}

}

- **Impacto**: Compromiso total del almacenamiento del contrato.

- Mitigación:

  - Control estricto de la dirección implementation

  - Uso de patrones proxy auditados
    ([EIP-1967](https://eips.ethereum.org/EIPS/eip-1967),
    [UUPS](https://docs.openzeppelin.com/contracts-stylus/uups-proxy))

A.1.4. Denegación de servicio (DoS)

Bloqueo de ejecución debido a fallos en llamadas externas o estructuras
no acotadas.

Código vulnerable

function payout(address\[\] memory recipients) public {

for (uint i = 0; i \< recipients.length; i++) {

payable(recipients\[i\]).transfer(1 ether);

}

}

- **Impacto**: Un solo fallo revierte toda la operación.

- Mitigación

  - Uso de [patrón *pull over
    push*](https://medium.com/@markojauregui/the-pull-over-push-model-in-solidity-a-secure-pattern-for-fund-withdrawals-10c2e6628626)

  - Evitar bucles dependientes de input externo

A.2. Vulnerabilidades técnicas de control y privilegios

A.2.1. Falta de control de acceso

Funciones críticas accesibles por cualquier usuario.

Código vulnerable

contract Ownable {

address public owner;

function withdrawAll() public {

payable(msg.sender).transfer(address(this).balance);

}

}

- **Impacto**: Pérdida total de fondos.

- Mitigación:

  - Uso de onlyOwner

  - Librerías como [OpenZeppelin
    AccessControl](https://docs.openzeppelin.com/contracts/5.x/access-control)

A.2.2. Uso de tx.origin

Uso incorrecto de tx.origin para autenticación.

Código vulnerable

function withdraw() public {

require(tx.origin == owner);

payable(msg.sender).transfer(address(this).balance);

}

- **Impacto**: Ataques mediante contratos intermediarios.

- **Mitigación**: Usar msg.sender para autenticación

A.2.3. Inicialización insegura (contratos upgradeables)

En contratos upgradeables, la inicialización se realiza mediante
funciones externas (initialize) en lugar de constructores. Si no están
protegidas, cualquier usuario puede ejecutarlas y asumir el control del
contrato.

Código vulnerable

function initialize(address \_owner) public {

owner = \_owner;

}

- **Impacto**: Un atacante puede inicializar el contrato antes que el
  legítimo propietario.

- Mitigación:

  - Uso de [initializer
    (OpenZeppelin)](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable)

  - Bloqueo de inicialización tras ejecución

A.3. Vulnerabilidades económicas y del entorno

A.3.1. Front-running / MEV

Un atacante observa la mempool y ejecuta transacciones antes que la
víctima.

Código vulnerable

function buy(uint price) public {

require(price == currentPrice);

// compra

}

- **Impacto**: Manipulación de operaciones (arbitraje, liquidaciones,
  subastas).

- Mitigación:

  - [*Commit-reveal*](https://medium.com/coinmonks/commit-reveal-scheme-in-solidity-c06eba4091bb)

  - Subastas ciegas

  - Uso de *relayers* privados

A.3.2. Dependencia de oráculos

Uso de datos externos manipulables.

Código vulnerable

function getPrice() public view returns (uint) {

return externalOracle.price();

}

- **Impacto**: Manipulación de precios en DeFi.

- Mitigación:

  - Oráculos descentralizados (ej. [Chainlink](https://chain.link/))

  - Promedios temporales
    ([TWAP](https://www.binance.com/es-MX/support/faq/detail/80655cc54d8a4b2bb8ea097001844fd1))

A.3.3. Uso de block.timestamp

El uso de block.timestamp como fuente de aleatoriedad o para decisiones
críticas es inseguro, ya que su valor puede ser parcialmente manipulado
por mineros o validadores dentro de ciertos límites.

Código vulnerable

function random() public view returns (uint) {

return uint(keccak256(abi.encodePacked(block.timestamp)));

}

- **Impacto**: Resultados predecibles o manipulables por
  mineros/validadores.

- Mitigación:

  - VRF ([Verifiable Random
    Functions](https://chain.link/education-hub/verifiable-random-function-vrf))

  - Fuentes externas verificables

A.4. Errores lógicos de negocio

A.4.1. Error en cálculo de balances

Errores en operadores lógicos o condiciones de validación pueden
provocar inconsistencias en la gestión de balances, especialmente en
casos límite donde las condiciones no cubren todos los escenarios
posibles.

Código vulnerable

function withdraw(uint amount) public {

require(balances\[msg.sender\] \> amount);

balances\[msg.sender\] -= amount;

}

- **Impacto**: Comportamiento incorrecto en condiciones límite.

- Mitigación:

  - Uso de \> en lugar de \>=.

A.4.2. Distribución incorrecta de recompensas

La lógica de distribución puede introducir errores debido a divisiones
enteras o falta de gestión de restos, provocando pérdida de precisión y
fondos no asignados correctamente.

Código vulnerable

function distribute() public {

uint reward = total / users.length;

for (uint i = 0; i \< users.length; i++) {

balances\[users\[i\]\] += reward;

}

}

- Impacto:

  - Pérdida de fondos debido a errores de redondeo (truncamiento en
    división entera)

  - Acumulación de saldo no distribuido en el contrato

  - Distribuciones injustas entre usuarios

  - Posibles vectores de explotación si un atacante manipula el número
    de participantes

- Mitigación:

  - Uso de patrones de distribución que gestionen residuos (por ejemplo,
    acumuladores o "*remainder handling*")

  - Empleo de mayor precisión mediante escalado ([*fixed-point
    arithmetic*](https://rareskills.io/post/solidity-fixed-point))

  - Validación de invariantes económicas (la suma distribuida debe
    coincidir con el total)

  - Testing específico de casos límite (número de usuarios, valores
    pequeños, etc.)

A.4.3. Estados inconsistentes

La falta de control adecuado sobre las transiciones de estado puede
permitir la ejecución de funciones en condiciones no válidas, generando
comportamientos inconsistentes en el contrato.

Código vulnerable

enum State { Open, Closed }

State public state;

function close() public {

state = State.Closed;

}

function bid() public payable {

require(state == State.Open);

}

- Impacto:

  - Ejecución de funciones en estados no válidos

  - Comportamiento inesperado del contrato

  - Bloqueo o bypass de lógica de negocio

  - Posible explotación combinada con otras vulnerabilidades (por
    ejemplo, *front-running* o *reentrancy*

- Mitigación:

  - Implementación de máquinas de estados explícitas y completas

  - Uso de modificadores para validar estado (inState(State.Open))

  - Restricción de transiciones de estado válidas

  - Aplicación de patrones [*state
    machines*](https://fravoll.github.io/solidity-patterns/state_machine.html)

A.5. Resumen de vulnerabilidades

  ------------------------------------------------------------------------------------------
  ID   Categoría   Vulnerabilidad   Tipo            Impacto    Detectable          Ejemplo
                                                               automáticamente     sección
  ---- ----------- ---------------- --------------- ---------- ------------------- ---------
  V1   Técnica     Reentrancy       Ejecución       Crítico    Sí                  A.1.1
                                                               (Slither/Mythril)   

  V2   Técnica     Overflow         Aritmético      Medio      Sí (Slither)        A.1.2

  V3   Técnica     Delegatecall     Ejecución       Crítico    Parcial             A.1.3

  V4   Control     Acceso no        Autorización    Crítico    Sí                  A.2.1
                   restringido                                                     

  V5   Control     tx.origin        Autenticación   Alto       Sí                  A.2.2

  V6   Económica   Front-running    MEV             Alto       No                  A.3.1

  V7   Económica   Oráculos         Dependencia     Crítico    No                  A.3.2
                                    externa                                        

  V8   Lógica      Error de balance Lógica          Variable   No                  A.4.1
  ------------------------------------------------------------------------------------------

# Entorno virtual Python {#entorno-virtual-python .Anexo}

### ¿Por qué usar entornos virtuales?

El desarrollo de una librería Python destinada a integrar múltiples
herramientas de análisis de seguridad plantea, desde el inicio, un
problema de gestión de dependencias que no debe subestimarse. Las
herramientas que se integran en la solución propuesta, como Slither,
Mythril o Echidna, tienen requisitos de versión específicos y en
ocasiones incompatibles entre sí cuando se instalan en el entorno global
del sistema. Esta situación, conocida en el ecosistema Python como
*dependency hell*, puede provocar conflictos silenciosos difíciles de
depurar y comprometer la reproducibilidad del entorno de desarrollo.

Un entorno virtual (*virtual environment*) es un directorio aislado que
contiene una instalación independiente del intérprete Python junto con
sus propios paquetes y dependencias, sin interferir con el sistema
global ni con otros proyectos. Esta separación proporciona varias
ventajas fundamentales en el contexto del presente trabajo:

En primer lugar, garantiza el **aislamiento de dependencias**, de forma
que cada proyecto mantiene sus propias versiones de bibliotecas sin
afectar al resto del sistema. Esto resulta especialmente relevante
cuando diferentes herramientas de análisis requieren versiones distintas
de una misma dependencia transitiva.

En segundo lugar, favorece la **reproducibilidad** del entorno de
desarrollo. Todos los integrantes del equipo pueden trabajar exactamente
con las mismas versiones de todas las dependencias, eliminando la
variabilidad asociada a instalaciones manuales y garantizando que los
resultados obtenidos durante el desarrollo son consistentes
independientemente del sistema operativo o configuración personal de
cada desarrollador.

En tercer lugar, facilita el **ciclo de vida del proyecto** al delimitar
claramente qué paquetes pertenecen al proyecto y cuáles son del sistema,
simplificando tanto la distribución de la librería como su posterior
publicación en registros públicos como PyPI.

### Tipos de entornos virtuales

En el ecosistema Python existen varias alternativas para la gestión de
entornos virtuales, con distintos niveles de abstracción y
funcionalidad.

El módulo estándar `venv`, incluido en la biblioteca estándar desde
Python 3.3, permite crear entornos virtuales básicos mediante el comando
`python -m venv .venv`. Sin embargo, este enfoque no incluye gestión de
dependencias ni ficheros de bloqueo (*lockfiles*), por lo que debe
complementarse con herramientas adicionales como `pip` y `pip-tools`.

`virtualenv` es una alternativa anterior al módulo estándar, con mayor
compatibilidad con versiones antiguas de Python y algunas
funcionalidades adicionales, aunque en la práctica ha quedado desplazada
por las herramientas modernas.

`conda` ofrece un modelo más completo que combina gestión de entornos
con gestión de paquetes, incluyendo dependencias no Python. Es habitual
en entornos científicos y de análisis de datos, pero introduce una
complejidad y un tamaño innecesarios para un proyecto centrado en el
ecosistema Python puro.

Herramientas como `poetry` o `pipenv` representan un nivel superior de
abstracción, combinando la gestión de entornos virtuales con la
resolución de dependencias, la generación de ficheros de bloqueo y el
ciclo de publicación de paquetes. Su adopción en proyectos profesionales
se ha generalizado en los últimos años.

Finalmente, `uv` constituye la herramienta de última generación en este
espacio, combinando todas las funcionalidades anteriores en una solución
de rendimiento muy superior, como se detalla en la sección siguiente.

### Herramienta a usar: uv

#### ¿Qué es uv?

`uv` es un gestor de paquetes y proyectos Python de alto rendimiento
desarrollado por Astral, la empresa creadora del formateador Ruff.
Implementado en Rust, se presenta como una herramienta unificada capaz
de sustituir a `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine` y
`virtualenv` mediante una interfaz de línea de comandos coherente. Su
desarrollo se orienta tanto a la velocidad de ejecución como a la
corrección en la resolución de dependencias y a la facilidad de adopción
en proyectos de diferente escala y complejidad.

#### Ventajas de uv

La principal ventaja diferencial de `uv` respecto a las alternativas
existentes es su rendimiento. Según los propios *benchmarks* publicados
en su documentación oficial, `uv` es entre 10 y 100 veces más rápido que
`pip` en operaciones de instalación de paquetes con caché caliente. Esta
diferencia resulta perceptible en la práctica, especialmente durante las
fases de incorporación de nuevos integrantes al equipo o en entornos de
integración continua donde el entorno debe reconstruirse frecuentemente.

Más allá del rendimiento, `uv` ofrece un conjunto de ventajas relevantes
para el desarrollo de la librería propuesta en este trabajo. Gestiona
automáticamente los entornos virtuales asociados a cada proyecto, sin
necesidad de crearlos ni activarlos manualmente. Genera y mantiene un
fichero de bloqueo universal (`uv.lock`) que garantiza instalaciones
reproducibles en cualquier plataforma. Permite gestionar múltiples
versiones del intérprete Python e instalar la versión adecuada de forma
automática si no está disponible en el sistema. Además, su diseño es
compatible con los estándares del ecosistema Python (`pyproject.toml`,
PEP 517, PEP 621), lo que facilita la integración con otras herramientas
y la publicación en registros de paquetes.

#### Qué proporciona uv en el contexto de este proyecto

Para el desarrollo de la librería propuesta, `uv` proporciona un
conjunto de funcionalidades que cubren todo el ciclo de vida del
proyecto, desde la inicialización hasta la publicación.

**Gestión de dependencias y sincronización del entorno.** Una vez
definidas las dependencias del proyecto en el fichero `pyproject.toml`,
cualquier integrante del equipo puede reproducir exactamente el mismo
entorno ejecutando un único comando:

    uv sync

Este comando resuelve las dependencias declaradas, instala las versiones
exactas registradas en el fichero de bloqueo `uv.lock` y configura el
entorno virtual del proyecto de forma automática. La simplicidad de este
flujo elimina los problemas habituales de divergencia entre entornos de
desarrollo individuales, garantizando que todos los miembros del equipo
trabajan con las mismas versiones de Slither, Mythril, Echidna y el
resto de dependencias de la librería.

**Inicialización de proyectos.** `uv` proporciona soporte integrado para
la creación de nuevos proyectos mediante el comando `uv init`. Para el
caso específico de una librería Python destinada a ser importada por
otros proyectos o publicada en PyPI, se utiliza la opción `--lib`:

    uv init --lib evmaudit

Este comando genera automáticamente la estructura de directorios
recomendada para una librería Python, incluyendo el fichero
`pyproject.toml` con los metadatos del proyecto, el directorio `src/`
con el paquete principal y los ficheros de configuración necesarios para
la construcción y distribución. El uso de la disposición `src/` (*src
layout*) es la práctica recomendada actualmente para proyectos
publicables, ya que evita problemas habituales relacionados con la
importación del paquete desde el directorio raíz durante el desarrollo.

**Construcción de distribuciones.** `uv` integra soporte nativo para la
generación de distribuciones instalables mediante el comando `uv build`,
que produce tanto el archivo fuente (*sdist*) como la rueda binaria
(*wheel*) del paquete:

    uv build

El resultado son los artefactos estándar de distribución Python ubicados
en el directorio `dist/`, listos para ser publicados o distribuidos
directamente.

**Publicación de paquetes.** El ciclo se completa con el soporte para
publicación en registros de paquetes, incluyendo PyPI, mediante el
comando `uv publish`:

    uv publish

Este comando gestiona la autenticación y la subida de los artefactos
generados, cubriendo el flujo completo que anteriormente requería
herramientas adicionales como `twine`.

En conjunto, `uv` unifica en una sola herramienta todo el ciclo de vida
del proyecto: inicialización, gestión de dependencias, sincronización
del entorno, construcción de distribuciones y publicación. Esta
integración reduce la fricción en el desarrollo colaborativo y facilita
la adopción de prácticas profesionales de gestión de proyectos Python
desde las primeras fases del trabajo.

# Distribución y Publicación en el Registro de Paquetes PyPI {#distribución-y-publicación-en-el-registro-de-paquetes-pypi .Anexo}

El ciclo de desarrollo de la librería propuesta culmina con su fase de
distribución, permitiendo que las herramientas de análisis de seguridad
implementadas sean accesibles e integrables por la comunidad de
desarrollo y auditoría de *smart contracts*. Para asegurar una
distribución estandarizada y eficiente dentro del ecosistema Python, se
ha seleccionado el índice oficial de paquetes PyPI (*Python Package
Index*). La gestión de este proceso se unifica bajo la herramienta `uv`,
garantizando la consistencia desde la compilación de los artefactos
hasta su publicación definitiva.

### Configuración de Metadatos del Proyecto (`pyproject.toml`)

El paso previo indispensable para la distribución consiste en la
definición inequívoca de los metadatos y la especificación del sistema
de construcción (*build system*) en el archivo de configuración
`pyproject.toml`, ubicado en la raíz del paquete. Este procedimiento se
rige bajo los estándares modernos de empaquetado de Python (PEP 517 y
PEP 621).

Para este proyecto, se ha adoptado `hatchling` como *build backend*,
debido a su ligereza, velocidad y compatibilidad nativa con las
especificaciones del ecosistema actual. A continuación, se presenta la
estructura de configuración requerida para delimitar las propiedades de
la librería `evmaudit`:

\[project\]

name = \"evmaudit\"

version = \"0.1.0\"

description = \"Add your description here\"

readme = \"README.md\"

authors = \[

{ name = \"Daniel Rovira Martínez\", email = \"pardalaco@gmail.com\" },

{ name = \"Paula Suárez Prieto\", email = \"Paula Suárez Prieto\" },

{ name = \"Adrián Moreno Martín\", email = \"adrimore2@gmail.com\" }

\]

requires-python = \"\>=3.12\"

dependencies = \[

\"eth\>=0.0.1\",

\"mythril\>=0.24.8\",

\"setuptools\<70.0.0\",

\"slither-analyzer\>=0.9.2\",

\"solc-select\>=1.2.0\",\]

\[project.scripts\]

evmaudit = \"evmaudit.main:main\"

\[build-system\]

requires = \[\"uv_build\>=0.11.15,\<0.12.0\"\]

build-backend = \"uv_build\"

Los clasificadores (*classifiers*) incluidos permiten categorizar la
librería dentro del índice público, facilitando su indexación en función
de la licencia de código abierto seleccionada, la compatibilidad del
sistema operativo y las versiones soportadas del intérprete Python.

### Proceso de Compilación del Paquete

Una vez validados los metadatos, se procede a la generación de los
archivos de distribución. Este proceso transforma el código fuente
estructurado en el directorio `src/` en artefactos instalables e
independientes del entorno de desarrollo.

La ejecución del comando unificado de compilación abstrae la complejidad
de las herramientas tradicionales:

uv build

Este comando genera de forma nativa dos tipos de distribuciones estándar
dentro del directorio `dist/`:

- **Distribución de código fuente (*sdist* o** `.tar.gz`**):** Un
  archivo comprimido que contiene el código fuente original y los
  archivos de configuración, actuando como respaldo para plataformas o
  configuraciones no previstas.

- **Distribución binaria compilada (*wheel* o** `.whl`**):** El formato
  de empaquetado moderno que permite una instalación directa y
  optimizada en el sistema destino, evitando la necesidad de compilar el
  código en la máquina del usuario final.

En contextos de desarrollo complejos donde el paquete forma parte de un
repositorio principal o arquitectura de *workspace* (como el entorno de
trabajo `TFM-UNIR`), `uv` permite gestionar la compilación de manera
localizada. Para forzar la construcción exclusiva del subproyecto desde
su propio directorio y evitar colisiones en la raíz global, se aplica la
opción de empaquetado específico:

    uv build --package evmaudit

### Seguridad y Autenticación en la Publicación

La publicación de código en repositorios públicos exige mecanismos
estrictos de control de acceso para prevenir vectores de ataque basados
en la cadena de suministro (*supply chain attacks*). Por razones de
seguridad, se desestima el uso de contraseñas de usuario tradicionales
en favor de la autenticación basada en **Tokens de API**.

El proceso de despliegue requiere la obtención de un *token* con prefijo
`pypi-` generado desde el panel de control de PyPI. En la primera
interacción, el alcance del *token* se configura de manera global; no
obstante, una vez realizada la primera subida con éxito, la buena
práctica metodológica dicta restringir los permisos del token de manera
exclusiva al ámbito del paquete `evmaudit`, minimizando así la
superficie de exposición en caso de compromiso de la credencial.

### Ejecución del Despliegue {#ejecución-del-despliegue-1}

Con los artefactos ubicados en el directorio `dist/` y las credenciales
expedidas, se procede a la transferencia segura hacia los servidores de
PyPI. El comando `uv publish` automatiza la verificación de integridad
mediante *hashes* criptográficos y realiza la subida en un único paso:

    uv publish

Durante el flujo interactivo en la línea de comandos, el sistema
requiere la introducción del identificador genérico `__token__` en el
campo de usuario, seguido de la clave alfanumérica del token de API en
el campo de contraseña. Con el objetivo de optimizar este flujo en
entornos de Integración Continua (CI/CD) o evitar la inserción manual
recurrente, es posible exportar temporalmente la credencial en el
entorno de la terminal actual:

    export UV_PUBLISH_TOKEN="pypi-tu-token-aqui"
    uv publish

Tras la finalización exitosa del proceso, el paquete queda registrado
globalmente, permitiendo su incorporación inmediata en otros proyectos
mediante los gestores tradicionales del ecosistema:

    pip install evmaudit

O bien, aprovechando los beneficios de rendimiento de la herramienta
unificada del proyecto:

    uv add evmaudit

### Ciclo de Mantenimiento y Actualización de Versiones

La evolución de la librería para la corrección de vulnerabilidades o la
integración de nuevas capacidades de análisis requiere una política
estricta de control de versiones. El flujo metodológico establecido para
la liberación de actualizaciones iterativas consta de tres fases
secuenciales:

- **Incremento del número de versión:** Modificación manual del campo
  `version` en el archivo `pyproject.toml` siguiendo el estándar de
  Versionado Semántico (ej. de `0.1.0` a `0.1.1`).

- **Saneamiento del directorio de distribución:** Eliminación de los
  artefactos obsoletos del directorio `dist/` para mitigar el riesgo de
  duplicidad o subidas erróneas de versiones previas.

- **Reconstrucción y despliegue:** Ejecución consecutiva de los procesos
  de empaquetado y transferencia:

<!-- -->

    uv build
    uv publish

Esta sistemática asegura que cada iteración de la herramienta de
auditoría de la EVM mantenga la trazabilidad, la coherencia histórica y
la disponibilidad pública necesarias para un entorno de producción
académica y profesional.

#  Entorno de Integración Continua (CI/CD) y Publicación Automatizada {#entorno-de-integración-continua-cicd-y-publicación-automatizada .Anexo}

Para garantizar la integridad del software durante el ciclo de vida del
desarrollo y agilizar el flujo de despliegue, se ha diseñado e
implementado un pipeline de Integración Continua (CI) basado en **GitHub
Actions**. Esta estrategia de ingeniería de software permite automatizar
la compilación, verificación y empaquetado de la aplicación en cada
iteración, mitigando los riesgos asociados a la integración manual de
código y asegurando la disponibilidad inmediata de artefactos listos
para producción.

### Arquitectura del Workflow y Disparadores (*Triggers*)

El flujo de trabajo automatizado se define de manera declarativa
mediante la sintaxis YAML de GitHub Actions. Con el propósito de
optimizar los recursos de cómputo y mantener un control estricto sobre
la estabilidad de la rama principal, se han configurado dos disparadores
específicos:

- **Eventos de Empuje (*Push*):** El pipeline se ejecuta de forma
  automática ante cualquier consolidación directa de código en la rama
  `main`, asegurando que cada incremento de software sea evaluado y
  empaquetado de inmediato.

- **Solicitudes de Extracción (*Pull Requests*):** La automatización
  actúa como una barrera de calidad (*quality gate*) ante cualquier
  intento de fusión hacia la rama `main`. Esto permite validar que las
  modificaciones propuestas por los desarrolladores no rompan el proceso
  de construcción del contenedor antes de que el código sea integrado
  definitivamente.

El entorno de ejecución seleccionado para los trabajos (*jobs*) es
`ubuntu-latest`, lo que proporciona un entorno virtual limpio, aislado y
actualizado de manera nativa por la infraestructura de GitHub.

### Desglose Técnico de las Etapas del Pipeline

El ciclo de vida del pipeline se divide en dos trabajos secuenciales y
dependientes, los cuales ejecutan tareas críticas de aprovisionamiento,
autenticación y despliegue:

![](media/image4.png){width="6.299305555555556in"
height="3.436111111111111in"}

#### Trabajo de Construcción y Publicación (`create-docker-image`)

Es el núcleo técnico de la automatización y consta de los siguientes
pasos detallados:

1.  **Clonación del Repositorio y Gestión de Submódulos:** Se utiliza la
    acción oficial `actions/checkout@v2`. Debido a la arquitectura
    desacoplada del proyecto, es indispensable configurar el parámetro
    `submodules: 'recursive'`. Esta directiva instruye al agente para
    que descargue e integre de manera automática el repositorio y código
    de `evmaudit` dentro de la estructura de directorios del pipeline.

2.  **Autenticación en el Registro de Contenedores (GHCR):** Mediante la
    acción `docker/login-action@v2`, el pipeline establece una conexión
    segura con el registro oficial de GitHub (`ghcr.io`). El proceso se
    autentica de forma dinámica utilizando el actor del ciclo de vida
    (`${{ github.actor }}`) y un token de acceso seguro almacenado de
    forma cifrada en los secretos del repositorio bajo la clave
    `${{ secrets.IMAGES_TFM_UNIR }}`.

3.  **Normalización del Espacio de Nombres y Doble Etiquetado
    (*Multi-tagging*):** Las especificaciones de Docker y el estándar de
    la Open Container Initiative (OCI) prohíben estrictamente el uso de
    caracteres en mayúscula para los nombres de las imágenes de
    contenedores. Para solucionar esto, el pipeline ejecuta un script en
    Bash que convierte dinámicamente el nombre del repositorio a
    minúsculas utilizando el comando `tr '[:upper:]' '[:lower:]'`.
    Posteriormente, se implementa una estrategia de doble etiquetado
    para optimizar la trazabilidad y la inmutabilidad:

    - **Etiqueta por SHA (**`IMAGE_SHA`**):** Vincula de forma unívoca
      el contenedor con el hash del *commit* específico de Git que
      originó la compilación (`${{ github.sha }}`). Esto permite
      realizar auditorías retrospectivas y despliegues deterministas en
      caso de fallos.

    - **Etiqueta de Última Versión (**`IMAGE_LATEST`**):** Sobrescribe
      el puntero `:latest` con la versión más reciente del software que
      haya superado la fase de construcción con éxito.

4.  **Construcción y *Push* Multiplataforma:** Se invoca de manera
    directa el comando `docker build`, forzando la compilación bajo la
    arquitectura destino `--platform linux/amd64` utilizando el
    `Dockerfile` del proyecto como plano de construcción. Una vez
    generadas las imágenes locales con sus respectivas etiquetas, se
    ejecutan las instrucciones de empuje (*push*) hacia el registro
    seguro de GitHub, quedando el artefacto disponible para su consumo.

#### Trabajo de Despliegue (`deploy`) y Limitaciones del Entorno

Para garantizar una separación formal de conceptos en la arquitectura de
la integración, el pipeline implementa un segundo trabajo secuencial
denominado `deploy`. Utilizando la directiva
`needs: create-docker-image`, se establece una restricción de
dependencia estricta: esta etapa no puede inicializarse si el
empaquetado y la publicación previa de la imagen en el registro han
fallado.

En la fase actual del proyecto, **esta etapa automatizada no ha sido
implementada de forma activa y opera estrictamente como un punto de
anclaje (*placeholder*) arquitectónico**. La justificación de esta
decisión de diseño radica en las limitaciones técnicas del entorno de
alojamiento seleccionado para las pruebas de concepto. La
infraestructura de EVMAudit se despliega externamente en la plataforma
PaaS **Railway** utilizando su modalidad de suscripción gratuita. Este
nivel de servicio impone restricciones en las interfaces de programación
(APIs) y en el uso de *webhooks*, impidiendo la ejecución de despliegues
totalmente automatizados (*Automated CD Triggers*) desencadenados de
forma directa mediante agentes de terceros como GitHub Actions.

Por consiguiente, el flujo de trabajo en este punto se limita a
verificar la integridad de la secuencia de comandos en consola, quedando
el aprovisionamiento de la infraestructura supeditado a los mecanismos
nativos de la plataforma de destino. En el **siguiente apartado (X.5.
Despliegue de la Infraestructura)**, se expondrá de manera más amplia la
configuración, el aprovisionamiento y las características operativas de
dicho entorno en Railway.

# Aplicación web desarrollada {#aplicación-web-desarrollada .Anexo}

# Contenedorización e Infraestructura de Despliegue (Docker) {#contenedorización-e-infraestructura-de-despliegue-docker .Anexo}

En el ámbito del desarrollo de software moderno y la ciberseguridad, la
reproducibilidad del entorno de ejecución constituye un pilar crítico.
Tradicionalmente, el despliegue de aplicaciones que integran múltiples
herramientas de análisis (como compiladores de Solidity y motores de
ejecución simbólica) se enfrentaba al problema de *\"funciona en mi
máquina\"*, derivado de las discrepancias en las versiones de las
dependencias, librerías del sistema operativo y configuraciones locales.
Para mitigar este riesgo, el presente proyecto adopta una arquitectura
basada en contenedores de aplicación a través del ecosistema de
**Docker** y **Docker Compose**.

1.  **Fundamentos de Contenedorización: Docker y Docker Compose**

Docker es una plataforma de código abierto basada en la tecnología de
contenedorización, la cual permite empaquetar una aplicación y todas sus
dependencias (binarios, librerías, archivos de configuración) en una
unidad estandarizada denominada **contenedor**. A diferencia de la
virtualización tradicional, Docker opera mediante la virtualización a
nivel de sistema operativo, compartiendo el núcleo (*kernel*) del
sistema anfitrión pero ejecutando los procesos en espacios de usuario
completamente aislados a través de *namespaces* y *cgroups*. Desde la
perspectiva de la seguridad, este aislamiento garantiza que los procesos
del pipeline de auditoría de EVMAudit se ejecuten de forma confinada,
mitigando el impacto en la infraestructura anfitriona ante la eventual
ejecución de código arbitrario o inesperado durante el análisis de
contratos inteligentes.

Por su parte, **Docker Compose** es la herramienta diseñada para definir
y orquestar aplicaciones Docker multi-contenedor. Mediante el uso de un
archivo de configuración declarativo en formato YAML
(docker-compose.yml), permite definir con precisión los servicios que
componen el sistema, sus dependencias de arranque, la exposición de
puertos hacia el exterior, la creación de redes aisladas y la asignación
de volúmenes persistentes. En el contexto de EVMAudit, actúa como el
motor de despliegue unificado, permitiendo al administrador inicializar
toda la infraestructura del TFM (servidor FastAPI, interfaz web y
almacenamiento de informes) de manera centralizada.

2.  **Estrategia de Construcción de la Imagen (Dockerfile)**

La construcción de la imagen se define en un único Dockerfile
optimizado. Debido a que el *pipeline* de análisis requiere interactuar
con el sistema operativo para invocar compiladores y binarios de
seguridad, se ha seleccionado **Ubuntu 22.04** como imagen base,
proporcionando un entorno estable y con soporte extendido para
dependencias nativas de Linux en arquitectura amd64.

El proceso de aprovisionamiento de la imagen se divide en las siguientes
fases críticas:

1.  **Entorno y Variables de Sistema:** Se configuran las variables de
    entorno PYTHONDONTWRITEBYTECODE=1 y PYTHONUNBUFFERED=1 para
    optimizar la ejecución de Python dentro del contenedor, evitando la
    escritura de residuos binarios y forzando el volcado de *logs* en
    tiempo real. Asimismo, se establece DEBIAN_FRONTEND=noninteractive
    para suprimir diálogos interactivos durante la instalación de
    paquetes.

2.  **Aprovisionamiento de Compiladores (Solidity):** Se añade el
    repositorio PPA oficial de Ethereum (ppa:ethereum/ethereum) para
    incorporar el compilador nativo de Solidity (solc). Posteriormente,
    se instala la utilidad solc-select mediante el gestor de paquetes de
    Python para automatizar la descarga y conmutación de versiones.

3.  **Integración del Fuzzer Echidna:** Dado que Echidna se distribuye
    de manera óptima como un binario estático para Linux, el contenedor
    automatiza su descarga directa (versión v2.3.2) desde los
    repositorios oficiales de *Crytic*, procediendo a su extracción e
    instalación en /usr/local/bin/ para garantizar su disponibilidad
    inmediata en el PATH del sistema.

4.  **Optimización de Dependencias con 'uv' (Multi-stage Build):** Con
    el objetivo de minimizar los tiempos de construcción y asegurar una
    gestión eficiente de los paquetes de Python, se emplea un mecanismo
    de construcción en etapas múltiples (*Multi-stage build*),
    importando los binarios optimizados del gestor uv directamente desde
    su imagen oficial en el registro de GitHub
    (ghcr.io/astral-sh/uv:latest).

5.  **Instalación del Paquete Local:** Tras establecer el directorio de
    trabajo en /app y copiar el código fuente , se ejecuta el comando uv
    sync \--frozen \--no-cache. Esto resuelve de forma determinista el
    grafo de dependencias del archivo uv.lock, registrando el paquete
    local editable evmaudit e instalando el servidor ASGI Uvicorn sin
    almacenar datos residuales en la caché de la imagen.

    1.  **Orquestación de Servicios (Docker Compose)**

La coordinación del contenedor web y sus dependencias con el sistema
anfitrión se gestiona de forma declarativa mediante un archivo
docker-compose.yml. La especificación del servicio, denominado
evmaudit-web, se fundamenta en tres pilares de ingeniería:

- **Persistencia de Datos mediante Volúmenes:** Con el fin de dotar al
  sistema de un estado persistente (pese a la naturaleza efímera de los
  contenedores), se realiza un mapeo directo de directorios del *host*
  hacia el contenedor:

- ./jsons/\_uploads:/app/jsons/\_uploads: Almacena de forma persistente
  los contratos Solidity cargados por los usuarios, los *wrappers*
  intermedios generados para Echidna y los informes de auditoría finales
  en formato JSON y Markdown.

- ./contracts:/app/contracts: Habilita un volumen opcional para la
  auditoría directa de Smart Contracts locales sin necesidad de
  interactuar con la interfaz web.

- **Aislamiento de Red y Mapeo de Puertos:** Se expone el puerto 8080
  del contenedor hacia el puerto 8080 del sistema anfitrión. Esto
  permite redirigir el tráfico HTTP de la interfaz construida en
  HTML5/Vanilla JS hacia el *backend* desarrollado en FastAPI de forma
  transparente.

- **Tolerancia a Fallos:** Se implementa la política de reinicio
  restart: unless-stopped. Esta directiva asegura la alta disponibilidad
  del servicio ante excepciones imprevistas en el motor de ejecución
  simbólica (Mythril) o caídas del propio demonio de Docker,
  garantizando que el servicio web vuelva a levantarse de manera
  automática salvo interrupción explícita del administrador.

  1.  **Flujo de Despliegue y Ciclo de Vida del Contenedor**

Para la puesta en marcha de la infraestructura local en entornos de
desarrollo o evaluación, el ciclo de vida del contenedor se administra
mediante el estándar de comandos de Docker Compose:

1.  **Fase de Construcción (Build):** Compilación de la imagen e
    instalación del entorno virtual determinista:

docker compose build

2.  **Fase de Inicialización (Up):** Despliegue e instanciación del
    servicio en segundo plano (*detached mode*):

docker compose up -d

3.  **Fase de Auditoría de Ejecución (Logs):** Inspección de la salida
    estándar del contenedor para la monitorización de los análisis en
    curso:

docker compose logs -f evmaudit-web

4.  **Fase de Parada (Down):** Interrupción y eliminación de los
    contenedores activos salvaguardando la integridad de los datos de
    las auditorías gracias a los volúmenes enlazados:

docker compose down

# Despliegue de la Infraestructura en la Nube (Railway)  {#despliegue-de-la-infraestructura-en-la-nube-railway .Anexo}

Para validar la operatividad de EVMAudit en un entorno accesible y
simular un escenario de producción real, se ha procedido al despliegue
de la arquitectura contenedorizada en la plataforma de Plataforma como
Servicio (PaaS) **Railway**. A continuación, se detallan las
especificaciones del entorno, las restricciones técnicas de hardware
identificadas y las optimizaciones de ingeniería aplicadas en el código
fuente para garantizar la estabilidad del sistema.

1.  **Aprovisionamiento y Configuración del Entorno Cloud**

El proceso de despliegue en la infraestructura de la nube se ha
estructurado bajo las siguientes directrices operativas:

- **Selección del Nivel de Servicio:** La instancia se ha instanciado
  haciendo uso del nivel gratuito (*Free Tier*) de la plataforma, el
  cual provee un crédito base de \$5 USD o un límite temporal de 30 días
  de cómputo.

- **Aislamiento Regional:** Con el objetivo de minimizar la latencia de
  red en las peticiones HTTP y optimizar la transferencia de datos, se
  ha seleccionado la región europea con nodo central en **Ámsterdam
  (EU)**.

- **Mapeo de Infraestructura y Orquestación:** El aprovisionamiento se
  realiza directamente vinculando el contenedor web a la imagen Docker
  compilada y almacenada en el registro de GitHub (ghcr.io), exponiendo
  de manera transparente la API del *backend* desarrollada en FastAPI.

- **Enrutamiento y Capa de Enlace (SSL):** La plataforma genera de
  manera dinámica un nombre de dominio completamente cualificado (FQDN)
  provisto de seguridad criptográfica TLS/SSL (HTTPS) para el acceso
  público a la interfaz de usuario:
  <https://evmaudit-production.up.railway.app/>.

  1.  **Limitaciones de Hardware y el Problema del Desbordamiento de
      Memoria (OOM)**

La modalidad gratuita de la plataforma PaaS impone restricciones
estrictas sobre los recursos de hardware asignados a cada contenedor,
parametrizados de la siguiente forma:

- **Capacidad de Cómputo (CPU):** 2 vCPU virtuales compartidas.

- **Memoria Volátil (RAM):** 1 GB con un límite estricto de cuota (*Plan
  Limit*).

Bajo un escenario de despliegue convencional en servidores dedicados o
infraestructura local, el pipeline de análisis de EVMAudit se ejecuta
sin restricciones debido a la disponibilidad de memoria elástica. Sin
embargo, en el entorno de la nube restringido, el motor de *fuzzing*
basado en propiedades **Echidna** presenta un problema crítico de
arquitectura.

Echidna, al estar desarrollado en Haskell, requiere de forma nativa una
reserva inicial y un espacio de intercambio que supera con creces el
gigabyte de memoria RAM para gestionar el mapa de cobertura del binario
y la generación de casos de prueba. Al alcanzar el umbral crítico de 1
GB asignado por Railway, el demonio del sistema operativo anfitrión
(*Kernel Out-of-Memory Killer*) destruía de manera abrupta el contenedor
para salvaguardar la integridad del nodo, provocando la caída del
servicio web y reportando un error de tipo *OOM*.

1.  **Optimización del Sistema en Tiempo de Ejecución (RTS) de Haskell**

Para mitigar el desbordamiento de memoria sin alterar las capacidades
analíticas esenciales de la herramienta, se realizó una intervención a
nivel de código en el módulo de control del *pipeline* (run_echidna). La
solución consistió en inyectar directivas específicas orientadas a
reconfigurar los parámetros del **Runtime System (RTS)** del compilador
de Glasgow Haskell (GHC) empaquetados dentro del binario de Echidna.

La estructura de invocación del proceso fue modificada e implementada en
Python mediante el siguiente diseño de argumentos:

command = \[\
\"echidna\",\
contract_path,\
\"\--contract\", contract_name,\
\"\--format\", \"json\",\
\
*\# Reducción del espacio de búsqueda del Fuzzer*\
\"\--test-limit\", \"100\",\
\
*\# Optimización de la compilación inicial*\
\"\--solc-args\", \"\--optimize-runs 0\",\
\
*\# Apertura de las opciones del Runtime System de Haskell*\
\"+RTS\",\
\
*\# Parámetros estrictos de control de memoria y concurrencia*\
\"-M950m\",\
\"-c\",\
\"-N1\",\
\
*\# Cierre de las opciones RTS*\
\"-RTS\"\
\]

A continuación se expone la justificación técnica detrás de los
modificadores inyectados:

- **Restricción de Ensayos (\--test-limit 100):** Al parametrizar el
  límite de pruebas en 100 iteraciones, se acota la profundidad del
  grafo de ejecución generado por el fuzzer. Esto reduce el consumo de
  memoria acumulativo a lo largo del tiempo de computación.

- **Techo Infranqueable de Memoria (-M950m):** Esta directiva establece
  que el asignador de memoria de Haskell tiene prohibido estrictamente
  reclamar más de 950 megabytes del espacio de usuario. Al situar este
  límite ligeramente por debajo del gigabyte real de Railway, se evita
  que el sistema operativo de la nube elimine el proceso por exceder la
  cuota física.

- **Recolección de Basura Agresiva (-c):** Activa un algoritmo de
  recolección de residuos más severo en el recolector de basura de
  Haskell (*Garbage Collector*). En lugar de acumular objetos
  intermedios en la memoria RAM, el sistema libera los recursos
  obsoletos inmediatamente después de cada evaluación de propiedad.

- **Concurrencia Confinada (-N1):** Limita la ejecución del entorno de
  ejecución a un único hilo de procesamiento, evitando la duplicación de
  estructuras de datos en memoria asociadas al paralelismo de hilos
  nativos.

Es importante destacar que la optimización descrita no se integró de
forma estática en la construcción del archivo Dockerfile (lo que habría
alterado el comportamiento de la imagen base de manera permanente), sino
que se aplicó directamente sobre el código fuente desplegado en el
contenedor en ejecución (*runtime*). Bajo condiciones de despliegue
convencionales en infraestructuras con escalabilidad elástica o recursos
dedicados de hardware, esta intervención técnica resultaría
completamente innecesaria, ya que la aplicación contaría con la memoria
suficiente para procesar el *pipeline* por defecto. Por consiguiente,
esta modificación responde de manera estricta a un mecanismo de
mitigación ad hoc, implementado exclusivamente para sortear las
limitaciones físicas del entorno gratuito y evitar la interrupción
forzada del servicio web por falta de memoria.

**Conclusión del Despliegue:** La implementación de estas salvaguardas
de bajo nivel ha permitido que la aplicación web de **EVMAudit** opere
de manera completamente estable y fluida en la nube. Pese a las severas
restricciones del entorno gratuito de Railway, el sistema es capaz de
completar con éxito el pipeline completo de auditoría en siete pasos sin
registrar caídas en el servicio ni excepciones por falta de recursos.
