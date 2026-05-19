```bash
pandoc Entrega_Borrador-2.docx -f docx -t markdown -o Borrador-2.md
```

![](media/image1.png){width="4.2034722222222225in"
height="0.9458333333333333in"}

Universidad Internacional de La Rioja

Escuela Superior de Ingeniería y Tecnología

Máster Universitario en Ciberseguridad

Título del Trabajo Fin de Estudios

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

En este apartado se introducirá un breve resumen en español del trabajo
realizado (extensión máxima 150 palabras). Este resumen debe incluir el
objetivo o propósito de la investigación, la metodología, los resultados
y las conclusiones.

El resumen debe contener lo qué se ha pretendido realizar (objetivo o
propósito de la investigación), cómo se ha realizado (método o proceso
desarrollado) y para qué se ha realizado (resultados y conclusiones).

**Importante:** En el caso de un TFE grupal, la extensión del TFE debe
garantizar que cada uno de los integrantes del equipo ha dedicado a la
elaboración y defensa del trabajo las competencias previstas en la
memoria. A modo orientativo, y para garantizar la calidad y dedicación
que requiere un TFE grupal, la extensión mínima ha de ser un 50%
superior a lo previsto para un TFE individual. Por lo tanto, la
extensión mínima en un TFE grupal es de **75 páginas**.

**Palabras clave:** Se deben incluir de 3 a 5 palabras claves en
español. Descriptores del trabajo que lo enmarcan en unas temáticas
determinadas.

Abstract

En este apartado se introducirá un breve resumen en **inglés** del
trabajo realizado (extensión máxima 150 palabras).

**Keywords**: Se deben incluir de 3 a 5 palabras claves en inglés

Índice de contenidos

[1. Introducción [1](#introducción)](#introducción)

[1.1. Motivación [2](#motivación)](#motivación)

[1.2. Planteamiento del problema
[3](#planteamiento-del-problema)](#planteamiento-del-problema)

[1.3. Estructura del trabajo
[4](#estructura-del-trabajo)](#estructura-del-trabajo)

[2. Estado del arte [6](#estado-del-arte)](#estado-del-arte)

[2.1. Fundamentos blockchain y contratos inteligentes
[6](#fundamentos-blockchain-y-contratos-inteligentes)](#fundamentos-blockchain-y-contratos-inteligentes)

[2.1.1. Tipos de redes blockchain
[7](#tipos-de-redes-blockchain)](#tipos-de-redes-blockchain)

[2.1.2. Consenso entre nodos
[8](#consenso-entre-nodos)](#consenso-entre-nodos)

[2.1.3. Fundamentos de contratos inteligentes
[9](#fundamentos-de-contratos-inteligentes)](#fundamentos-de-contratos-inteligentes)

[2.1.4. Ethereum Virtual Machine
[10](#ethereum-virtual-machine)](#ethereum-virtual-machine)

[2.1.5. Propiedades de los contratos inteligentes
[10](#propiedades-de-los-contratos-inteligentes)](#propiedades-de-los-contratos-inteligentes)

[2.1.6. Limitaciones y riesgos
[11](#limitaciones-y-riesgos)](#limitaciones-y-riesgos)

[2.1.7. Aplicaciones descentralizadas (DApps)
[11](#aplicaciones-descentralizadas-dapps)](#aplicaciones-descentralizadas-dapps)

[2.2. Finanzas Descentralizadas (DeFi): ecosistema y riesgo estructural
[12](#finanzas-descentralizadas-defi-ecosistema-y-riesgo-estructural)](#finanzas-descentralizadas-defi-ecosistema-y-riesgo-estructural)

[2.3. Interoperabilidad blockchain: bridges y protocolos cross-chain
[13](#interoperabilidad-blockchain-bridges-y-protocolos-cross-chain)](#interoperabilidad-blockchain-bridges-y-protocolos-cross-chain)

[2.3.1. El problema de las blockchains aisladas
[13](#el-problema-de-las-blockchains-aisladas)](#el-problema-de-las-blockchains-aisladas)

[2.3.2. Tipos de bridges y arquitecturas
[14](#tipos-de-bridges-y-arquitecturas)](#tipos-de-bridges-y-arquitecturas)

[2.3.3. Componentes técnicos de un bridge
[15](#componentes-técnicos-de-un-bridge)](#componentes-técnicos-de-un-bridge)

[2.4. Herramientas de Análisis
[17](#herramientas-de-análisis)](#herramientas-de-análisis)

[2.4.1. Slither [17](#slither)](#slither)

[2.4.2. Mythril --- Ejecución Simbólica (ConsenSys)
[19](#mythril-ejecución-simbólica-consensys)](#mythril-ejecución-simbólica-consensys)

[2.4.3. Echidna --- Fuzzing Basado en Propiedades (Trail of Bits)
[22](#echidna-fuzzing-basado-en-propiedades-trail-of-bits)](#echidna-fuzzing-basado-en-propiedades-trail-of-bits)

[2.5. Síntesis y limitaciones del estado del arte
[24](#síntesis-y-limitaciones-del-estado-del-arte)](#síntesis-y-limitaciones-del-estado-del-arte)

[2.6. Vulnerabilidades de seguridad en contratos inteligentes de
Ethereum
[25](#vulnerabilidades-de-seguridad-en-contratos-inteligentes-de-ethereum)](#vulnerabilidades-de-seguridad-en-contratos-inteligentes-de-ethereum)

[2.6.1. Vulnerabilidades técnicas de ejecución
[25](#vulnerabilidades-técnicas-de-ejecución)](#vulnerabilidades-técnicas-de-ejecución)

[2.6.2. Vulnerabilidades de control y privilegios
[26](#vulnerabilidades-de-control-y-privilegios)](#vulnerabilidades-de-control-y-privilegios)

[2.6.3. Vulnerabilidades económicas y dependencia del entorno
[26](#vulnerabilidades-económicas-y-dependencia-del-entorno)](#vulnerabilidades-económicas-y-dependencia-del-entorno)

[2.6.4. Errores lógicos de negocio
[27](#errores-lógicos-de-negocio)](#errores-lógicos-de-negocio)

[2.6.5. Conclusión [27](#conclusión)](#conclusión)

[2.7. Ataques Reales [28](#ataques-reales)](#ataques-reales)

[2.7.1. Vulnerabilidad técnica de ejecución: The DAO (2016)
[28](#vulnerabilidad-técnica-de-ejecución-the-dao-2016)](#vulnerabilidad-técnica-de-ejecución-the-dao-2016)

[2.7.2. Vulnerabilidad de control y privilegios: Poly Network (2021)
[29](#vulnerabilidad-de-control-y-privilegios-poly-network-2021)](#vulnerabilidad-de-control-y-privilegios-poly-network-2021)

[2.7.3. Vulnerabilidad económica y dependencia del entorno: bZx (2020)
[30](#vulnerabilidad-económica-y-dependencia-del-entorno-bzx-2020)](#vulnerabilidad-económica-y-dependencia-del-entorno-bzx-2020)

[2.7.4. Error lógico de negocio: Euler Finance (2023)
[31](#error-lógico-de-negocio-euler-finance-2023)](#error-lógico-de-negocio-euler-finance-2023)

[3. Objetivos concretos y metodología de trabajo
[32](#objetivos-concretos-y-metodología-de-trabajo)](#objetivos-concretos-y-metodología-de-trabajo)

[3.1. Objetivo general [32](#objetivo-general)](#objetivo-general)

[3.2. Objetivos específicos
[32](#objetivos-específicos)](#objetivos-específicos)

[3.3. Metodología del trabajo
[33](#metodología-del-trabajo)](#metodología-del-trabajo)

[4. Desarrollo específico de la contribución
[36](#desarrollo-específico-de-la-contribución)](#desarrollo-específico-de-la-contribución)

[4.1. Tipo 2. Desarrollo de software
[36](#tipo-2.-desarrollo-de-software)](#tipo-2.-desarrollo-de-software)

[4.1.1. Identificación de requisitos
[36](#identificación-de-requisitos)](#identificación-de-requisitos)

[4.1.2. Descripción de la herramienta software desarrollada
[36](#descripción-de-la-herramienta-software-desarrollada)](#descripción-de-la-herramienta-software-desarrollada)

[4.1.3. Evaluación [36](#evaluación)](#evaluación)

[5. Conclusiones y trabajo futuro
[37](#conclusiones-y-trabajo-futuro)](#conclusiones-y-trabajo-futuro)

[Referencias bibliográficas
[38](#referencias-bibliográficas)](#referencias-bibliográficas)

[Anexo A. Ejemplos de vulnerabilidades en contratos inteligentes
[43](#ejemplos-de-vulnerabilidades-en-contratos-inteligentes)](#ejemplos-de-vulnerabilidades-en-contratos-inteligentes)

Índice de figuras

[Figura 1. *Cadena genérica de bloques*
[2](#_Toc227683447)](#_Toc227683447)

Índice de tablas

[Tabla 1. *Organización del trabajo en grupo.*
[VIII](#_Toc150422790)](#_Toc150422790)

[Tabla 2. *Ejemplo de tabla con sus principales elementos.*
[2](#_Toc150422791)](#_Toc150422791)

Organización del trabajo en grupo

En este apartado se detallarán las distintas partes en las que se ha
dividido el trabajo entre los componentes del grupo, los objetivos
perseguidos en cada una de ellas y los mecanismos de coordinación
empleados. Este apartado deberá ser validado por el director para poder
comenzar con el trabajo.

Partes que aborda el TFE, distribución y estructura de la memoria

Cada estudiante debe abordar elementos/partes que, individualmente,
podrían suponer un TFE por sí mismas.

Complete la siguiente tabla que debe reflejar el reparto de trabajo a la
hora de confeccionar la memoria del TFE.

+-----------------------------------------------------------------------------------+
| Organización del trabajo en grupo - Desarrollo de la memoria                      |
+:===========================================:+:===================================:+
| Apartado de la memoria                      | **Responsables**                    |
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

: []{#_Toc150422790 .anchor}Tabla 1. *Organización del trabajo en
grupo.*

Fuente: Elaboración propia.

Objetivo del TFE desde el punto de vista de la adquisición de
conocimientos

Desde el punto de vista de la adquisición de conocimientos, este TFE,
incorpora varios segmentos suficientemente diferenciados que, en sí
mismos, podrían haber sido tema para una propuesta de investigación
individual; con ello los estudiantes alcanzarían una
multidisciplinariedad que trasvasa de lo estrictamente teórico a lo
empírico. Lo que le aporta el carácter grupal del trabajo es, por lo
tanto, un carácter holístico que le da relevancia no solo académica sino
práctica, pues termina siendo un resultado utilizable profesionalmente
por los estudiantes en su ámbito de trabajo.

Mecanismos de coordinación empleados

Recordar que nos estamos preparando para un día a día en un mundo
laboral cada vez más complejo. Este mundo laboral implica siempre
trabajar en conjunto con otras personas y profesionales de diferentes
ámbitos. Un TFE grupal te prepara para esa realidad a la que nos
enfrentamos en un entorno laboral real.

Describir los mecanismos y herramientas de coordinación y comunicación
empleados para el desarrollo del TFE grupal.

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
pretende contribuir al estudio de técnicas de análisis aplicadas a smart
contracts y explorar enfoques que permitan mejorar la automatización de
auditorías de seguridad en entornos blockchain.

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

![[]{#_Toc227683447 .anchor}Figura 1. *Cadena genérica de
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

**Arquitectura y Funcionamiento**

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

## Tipo 2. Desarrollo de software

### Identificación de requisitos

### Descripción de la herramienta software desarrollada

### Evaluación

# Conclusiones y trabajo futuro

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
Ethereum smart contracts (SoK)," *Lecture Notes in Computer Science
(including subseries Lecture Notes in Artificial Intelligence and
Lecture Notes in Bioinformatics)*, vol. 10204 LNCS, pp. 164--186, 2017,
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

**Código vulnerable**

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

- **Mitigación**:

  - Patrón
    [*Checks-Effects-Interactions*](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)

  - Uso de ReentrancyGuard

  - Actualizar el estado antes de llamadas externas

A.1.2. Integer Overflow / Underflow

Errores aritméticos que provocan desbordamientos en operaciones enteras.
Aunque mitigados en Solidity ≥0.8, siguen siendo relevantes en bloques
unchecked.

**Código vulnerable**

function increment(uint256 x) public pure returns (uint256) {

unchecked {

return x + 1;

}

}

- **Impacto**: Puede alterar balances o condiciones lógicas críticas.

- **Mitigación**:

  - Evitar unchecked salvo casos justificados

  - Uso de validaciones explícitas

A.1.3. Uso inseguro de delegatecall

La función delegatecall ejecuta código externo en el contexto de
almacenamiento del contrato llamador.

**Código vulnerable**

contract Proxy {

address public implementation;

function execute(bytes memory data) public {

(bool success, ) = implementation.delegatecall(data);

require(success);

}

}

- **Impacto**: Compromiso total del almacenamiento del contrato.

- **Mitigación**:

  - Control estricto de la dirección implementation

  - Uso de patrones proxy auditados
    ([EIP-1967](https://eips.ethereum.org/EIPS/eip-1967),
    [UUPS](https://docs.openzeppelin.com/contracts-stylus/uups-proxy))

A.1.4. Denegación de servicio (DoS)

Bloqueo de ejecución debido a fallos en llamadas externas o estructuras
no acotadas.

**Código vulnerable**

function payout(address\[\] memory recipients) public {

for (uint i = 0; i \< recipients.length; i++) {

payable(recipients\[i\]).transfer(1 ether);

}

}

- **Impacto**: Un solo fallo revierte toda la operación.

- **Mitigación**

  - Uso de [patrón *pull over
    push*](https://medium.com/@markojauregui/the-pull-over-push-model-in-solidity-a-secure-pattern-for-fund-withdrawals-10c2e6628626)

  - Evitar bucles dependientes de input externo

A.2. Vulnerabilidades técnicas de control y privilegios

A.2.1. Falta de control de acceso

Funciones críticas accesibles por cualquier usuario.

**Código vulnerable**

contract Ownable {

address public owner;

function withdrawAll() public {

payable(msg.sender).transfer(address(this).balance);

}

}

- **Impacto**: Pérdida total de fondos.

- **Mitigación**:

  - Uso de onlyOwner

  - Librerías como [OpenZeppelin
    AccessControl](https://docs.openzeppelin.com/contracts/5.x/access-control)

A.2.2. Uso de tx.origin

Uso incorrecto de tx.origin para autenticación.

**Código vulnerable**

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

**Código vulnerable**

function initialize(address \_owner) public {

owner = \_owner;

}

- **Impacto**: Un atacante puede inicializar el contrato antes que el
  legítimo propietario.

- **Mitigación**:

  - Uso de [initializer
    (OpenZeppelin)](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable)

  - Bloqueo de inicialización tras ejecución

A.3. Vulnerabilidades económicas y del entorno

A.3.1. Front-running / MEV

Un atacante observa la mempool y ejecuta transacciones antes que la
víctima.

**Código vulnerable**

function buy(uint price) public {

require(price == currentPrice);

// compra

}

- **Impacto**: Manipulación de operaciones (arbitraje, liquidaciones,
  subastas).

- **Mitigación**:

  - [*Commit-reveal*](https://medium.com/coinmonks/commit-reveal-scheme-in-solidity-c06eba4091bb)

  - Subastas ciegas

  - Uso de *relayers* privados

A.3.2. Dependencia de oráculos

Uso de datos externos manipulables.

**Código vulnerable**

function getPrice() public view returns (uint) {

return externalOracle.price();

}

- **Impacto**: Manipulación de precios en DeFi.

- **Mitigación**:

  - Oráculos descentralizados (ej. [Chainlink](https://chain.link/))

  - Promedios temporales
    ([TWAP](https://www.binance.com/es-MX/support/faq/detail/80655cc54d8a4b2bb8ea097001844fd1))

A.3.3. Uso de block.timestamp

El uso de block.timestamp como fuente de aleatoriedad o para decisiones
críticas es inseguro, ya que su valor puede ser parcialmente manipulado
por mineros o validadores dentro de ciertos límites.

**Código vulnerable**

function random() public view returns (uint) {

return uint(keccak256(abi.encodePacked(block.timestamp)));

}

- **Impacto**: Resultados predecibles o manipulables por
  mineros/validadores.

- **Mitigación**:

  - VRF ([Verifiable Random
    Functions](https://chain.link/education-hub/verifiable-random-function-vrf))

  - Fuentes externas verificables

A.4. Errores lógicos de negocio

A.4.1. Error en cálculo de balances

Errores en operadores lógicos o condiciones de validación pueden
provocar inconsistencias en la gestión de balances, especialmente en
casos límite donde las condiciones no cubren todos los escenarios
posibles.

**Código vulnerable**

function withdraw(uint amount) public {

require(balances\[msg.sender\] \> amount);

balances\[msg.sender\] -= amount;

}

- **Impacto**: Comportamiento incorrecto en condiciones límite.

- **Mitigación**:

  - Uso de \> en lugar de \>=.

A.4.2. Distribución incorrecta de recompensas

La lógica de distribución puede introducir errores debido a divisiones
enteras o falta de gestión de restos, provocando pérdida de precisión y
fondos no asignados correctamente.

**Código vulnerable**

function distribute() public {

uint reward = total / users.length;

for (uint i = 0; i \< users.length; i++) {

balances\[users\[i\]\] += reward;

}

}

- **Impacto**:

  - Pérdida de fondos debido a errores de redondeo (truncamiento en
    división entera)

  - Acumulación de saldo no distribuido en el contrato

  - Distribuciones injustas entre usuarios

  - Posibles vectores de explotación si un atacante manipula el número
    de participantes

- **Mitigación**:

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

**Código vulnerable**

enum State { Open, Closed }

State public state;

function close() public {

state = State.Closed;

}

function bid() public payable {

require(state == State.Open);

}

- **Impacto**:

  - Ejecución de funciones en estados no válidos

  - Comportamiento inesperado del contrato

  - Bloqueo o bypass de lógica de negocio

  - Posible explotación combinada con otras vulnerabilidades (por
    ejemplo, *front-running* o *reentrancy*

- **Mitigación**:

  - Implementación de máquinas de estados explícitas y completas

  - Uso de modificadores para validar estado (inState(State.Open))

  - Restricción de transiciones de estado válidas

  - Aplicación de patrones [*state
    machines*](https://fravoll.github.io/solidity-patterns/state_machine.html)

A.5. Resumen de vulnerabilidades

  ------------------------------------------------------------------------------------------
   ID   Categoría   Vulnerabilidad       Tipo        Impacto       Detectable       Ejemplo
                                                                 automáticamente    sección
  ---- ----------- ---------------- --------------- ---------- ------------------- ---------
   V1    Técnica      Reentrancy       Ejecución     Crítico           Sí            A.1.1
                                                                (Slither/Mythril)  

   V2    Técnica       Overflow       Aritmético      Medio       Sí (Slither)       A.1.2

   V3    Técnica     Delegatecall      Ejecución     Crítico         Parcial         A.1.3

   V4    Control      Acceso no      Autorización    Crítico           Sí            A.2.1
                     restringido                                                   

   V5    Control      tx.origin      Autenticación     Alto            Sí            A.2.2

   V6   Económica   Front-running         MEV          Alto            No            A.3.1

   V7   Económica      Oráculos       Dependencia    Crítico           No            A.3.2
                                        externa                                    

   V8    Lógica    Error de balance     Lógica       Variable          No            A.4.1
  ------------------------------------------------------------------------------------------
