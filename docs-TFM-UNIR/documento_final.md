

---
title: "EVMAudit: Librería multiherramienta para la detección automatizada de vulnerabilidades en contratos inteligentes de Ethereum"
author:
  - "Daniel Rovira Martínez"
  - "Paula Suárez Prieto"
  - "Adrián Moreno Martín"
toc: true
toc-depth: 3
toc-title: "Índice de Contenidos"
---
# Resumen

La seguridad de los contratos inteligentes se ha convertido en un aspecto crítico dentro del ecosistema blockchain debido al elevado impacto económico que pueden provocar las vulnerabilidades presentes en este tipo de software. Aunque existen herramientas especializadas para su análisis, como Slither, Mythril o Echidna, sus resultados suelen presentarse de forma heterogénea y con dificultades para correlacionar y priorizar los hallazgos obtenidos. En este Trabajo Fin de Máster se presenta EVMAudit, una librería desarrollada en Python orientada a la ejecución conjunta de múltiples herramientas de análisis de seguridad para contratos inteligentes compatibles con la Ethereum Virtual Machine (EVM). La solución propuesta incorpora mecanismos de normalización, correlación y priorización de resultados, permitiendo ofrecer una visión unificada y más estructurada de las vulnerabilidades detectadas. Además, la herramienta se distribuye mediante PyPI y dispone de una infraestructura de despliegue y automatización basada en Docker y CI/CD.

Palabras clave: contratos inteligentes, Ethereum, ciberseguridad, análisis de vulnerabilidades, blockchain

# Abstract
Smart contract security has become a critical concern within the blockchain ecosystem due to the significant economic impact caused by software vulnerabilities. Although several specialized analysis tools, such as Slither, Mythril, and Echidna, are available, their results are often heterogeneous and difficult to correlate and prioritize. This Master's Thesis presents EVMAudit, a Python library designed to orchestrate multiple security analysis tools for Ethereum Virtual Machine (EVM) compatible smart contracts. The proposed solution includes mechanisms for result normalization, correlation, and prioritization, providing a unified and more structured view of the detected vulnerabilities. Furthermore, the tool is distributed through PyPI and includes an automated deployment infrastructure based on Docker and CI/CD practices.

Keywords: smart contracts, Ethereum, cybersecurity, vulnerability analysis, blockchain

\newpage
## Mecanismos de coordinación empleados

Con el objetivo de garantizar un seguimiento continuo del trabajo y mantener la coordinación entre los miembros del grupo, se estableció una reunión interna semanal en la que cada integrante exponía las tareas realizadas durante el periodo correspondiente y las posibles dificultades encontradas. Estas reuniones permitían, además, debatir las siguientes líneas de trabajo y planificar las tareas a desarrollar en las semanas posteriores.

Como herramientas de comunicación y colaboración se utilizaron principalmente WhatsApp para la comunicación diaria, Microsoft Teams para la realización de reuniones telemáticas, un repositorio compartido en GitHub para la gestión y sincronización del código fuente, y un documento compartido de Microsoft Word para la elaboración conjunta de la memoria.

Adicionalmente, tras cada una de las entregas parciales previstas en la planificación del Trabajo Fin de Máster, se mantuvo una reunión de seguimiento con el director del trabajo. Estas sesiones permitieron revisar el progreso realizado, recibir retroalimentación sobre los resultados obtenidos y definir las acciones necesarias para las siguientes fases del proyecto.


\newpage


# 1. Introducción

La tecnología blockchain ha evolucionado significativamente desde la aparición de Bitcoin en 2008 como sistema de dinero electrónico descentralizado. Con la llegada de plataformas como Ethereum, blockchain dejó de utilizarse únicamente para la transferencia de activos digitales y pasó a convertirse en una infraestructura capaz de ejecutar aplicaciones descentralizadas mediante contratos inteligentes. Estos contratos permiten automatizar lógica de negocio y gestionar activos sin necesidad de intermediarios, lo que ha impulsado el crecimiento de sectores como las finanzas descentralizadas (DeFi), los sistemas de tokenización y los protocolos de interoperabilidad blockchain.

Sin embargo, este nuevo paradigma también introduce importantes desafíos desde el punto de vista de la ciberseguridad. Los contratos inteligentes operan en entornos públicos y adversariales, donde el código es accesible para cualquier usuario y los errores pueden ser analizados y explotados por actores maliciosos. Además, la inmutabilidad de la blockchain dificulta la corrección de vulnerabilidades una vez desplegados los contratos, aumentando el impacto potencial de cualquier fallo de seguridad.

Durante los últimos años, múltiples incidentes han demostrado las consecuencias reales de estas vulnerabilidades. Ataques como The DAO, Poly Network, bZx o Euler Finance provocaron pérdidas económicas de cientos de millones de dólares y evidenciaron que los errores en contratos inteligentes no solo afectan al software, sino también a activos digitales con valor económico directo.

En este contexto, el análisis de seguridad de contratos inteligentes se ha convertido en una de las áreas más relevantes dentro de la ciberseguridad blockchain. Actualmente existen distintas herramientas especializadas que permiten detectar vulnerabilidades mediante técnicas como análisis estático, ejecución simbólica o fuzzing. No obstante, estas soluciones presentan limitaciones importantes, entre las que destacan la elevada tasa de falsos positivos, la fragmentación de resultados y la dificultad para priorizar riesgos de manera efectiva.

El presente Trabajo Fin de Máster se centra en el diseño e implementación de una librería en Python orientada al análisis de seguridad de contratos inteligentes compatibles con la Ethereum Virtual Machine (EVM). La propuesta busca integrar distintas herramientas de análisis existentes en una arquitectura modular capaz de correlacionar hallazgos, normalizar resultados heterogéneos y facilitar una evaluación más útil y estructurada de las vulnerabilidades detectadas.

La finalidad del trabajo no es reemplazar las herramientas actuales, sino proporcionar una capa adicional de correlación y análisis que mejore la interpretación de resultados y reduzca algunas de las limitaciones presentes en el estado del arte. Para ello, se estudiarán las principales técnicas de auditoría de smart contracts, las vulnerabilidades más relevantes en Solidity y las herramientas más utilizadas en entornos profesionales y académicos.

Finalmente, el trabajo incluirá el diseño de la arquitectura de la solución propuesta, su implementación como librería software y una evaluación experimental utilizando contratos vulnerables conocidos y casos reales de código abierto.

## 1.1. Motivación

La auditoría de contratos inteligentes se ha convertido en una necesidad crítica dentro del ecosistema blockchain debido al creciente volumen económico gestionado por aplicaciones descentralizadas y protocolos DeFi. En este contexto, la detección temprana de vulnerabilidades resulta fundamental para reducir riesgos de explotación y minimizar pérdidas económicas.

Actualmente existen diversas herramientas orientadas al análisis automatizado de contratos inteligentes, como Slither, Mythril o Echidna, que aplican técnicas de análisis diferentes y complementarias. Sin embargo, su utilización conjunta continúa presentando dificultades relevantes. Cada herramienta genera resultados con formatos, niveles de detalle y criterios de severidad distintos, lo que dificulta la correlación de hallazgos y obliga a realizar revisiones manuales adicionales durante el proceso de auditoría.

Además, muchas soluciones actuales producen un elevado número de falsos positivos o detectan vulnerabilidades redundantes, complicando la priorización efectiva de riesgos. Esta situación provoca que los auditores deban invertir una cantidad significativa de tiempo en interpretar resultados y validar manualmente la relevancia real de cada hallazgo.

La motivación principal de este trabajo surge de la necesidad de mejorar este proceso mediante una solución que permita integrar y normalizar información procedente de múltiples herramientas de análisis. Se busca proporcionar una visión más estructurada y útil del estado de seguridad de un contrato inteligente, facilitando tanto la interpretación de resultados como la identificación de vulnerabilidades relevantes.

Desde el punto de vista académico y profesional, el trabajo también pretende contribuir al estudio de técnicas de análisis aplicadas a contratos inteligentes y explorar enfoques que permitan mejorar la automatización de auditorías de seguridad en entornos blockchain.

## 1.2. Planteamiento del problema

El análisis de seguridad de contratos inteligentes presenta dificultades específicas derivadas tanto del modelo de ejecución de blockchain como de las limitaciones de las herramientas actuales de auditoría automática.

Por un lado, los contratos inteligentes operan en un entorno especialmente adversarial. El código fuente y el bytecode suelen ser públicos, las transacciones son observables y los atacantes pueden estudiar el comportamiento interno de los contratos antes de explotar una vulnerabilidad. Además, la ejecución determinista de la Ethereum Virtual Machine y la inmutabilidad del despliegue implican que muchos errores no puedan corregirse fácilmente una vez publicados en la red.

Por otro lado, las herramientas automáticas de análisis existentes presentan limitaciones relevantes. Soluciones ampliamente utilizadas como Slither, Mythril o Echidna aplican técnicas diferentes y generan resultados heterogéneos tanto en formato como en nivel de detalle. Esto provoca problemas como:

- Detección redundante de una misma vulnerabilidad por múltiples
  herramientas.
- Generación de falsos positivos.
- Dificultad para correlacionar hallazgos relacionados.
- Ausencia de criterios homogéneos de priorización.
- Escasa contextualización del impacto real de las vulnerabilidades.

Como consecuencia, los procesos de auditoría continúan dependiendo en gran medida de la revisión manual realizada por expertos, especialmente para validar resultados y diferenciar vulnerabilidades críticas de hallazgos con impacto reducido.

Ante esta situación, el problema abordado en este trabajo consiste en cómo mejorar el análisis automatizado de contratos inteligentes mediante un sistema capaz de integrar múltiples herramientas de seguridad, normalizar sus resultados y proporcionar una visión más estructurada y útil de las vulnerabilidades detectadas.

Para ello, se propone el desarrollo de una librería en Python orientada a la correlación de hallazgos de seguridad en contratos inteligentes compatibles con la EVM, utilizando un enfoque modular que facilite la integración de distintas técnicas de análisis.

## 1.3. Estructura del trabajo

El presente documento se organiza en varios capítulos que permiten abordar de forma progresiva tanto el contexto teórico del problema como el desarrollo de la solución propuesta.

En primer lugar, el capítulo de introducción presenta el contexto general del trabajo, la motivación del estudio y el problema identificado.

A continuación, el capítulo correspondiente al estado del arte recoge los fundamentos necesarios para comprender el análisis de seguridad en contratos inteligentes. En este apartado se abordan conceptos relacionados con blockchain, Ethereum, contratos inteligentes, así como las principales vulnerabilidades de seguridad, técnicas de auditoría y herramientas de análisis existentes en la actualidad.

Posteriormente, el capítulo de objetivos concretos y metodología de trabajo define el objetivo general del TFM, los objetivos específicos y las distintas fases planteadas para el desarrollo de la solución propuesta. También se describe el enfoque metodológico utilizado para la investigación, diseño, implementación y validación del sistema.

El capítulo de desarrollo específico de la contribución constituye el núcleo principal del trabajo. En él se describe el diseño e implementación de la librería desarrollada, incluyendo la arquitectura del sistema, los módulos principales, la integración de herramientas externas, el proceso de normalización y correlación de resultados y los mecanismos de evaluación empleados.

Finalmente, el capítulo de conclusiones y trabajo futuro recoge las principales aportaciones del trabajo, las limitaciones identificadas durante el desarrollo y posibles líneas de mejora o evolución futura de la herramienta propuesta.

\newpage


# 2. Estado del arte
El presente capítulo recoge los fundamentos técnicos y el contexto necesario para comprender el problema abordado en este Trabajo Fin de Máster. En primer lugar, se introducen los conceptos básicos de blockchain y contratos inteligentes, con especial atención a Ethereum y al modelo de ejecución de la Ethereum Virtual Machine. Posteriormente, se analizan los principales retos de seguridad asociados a los contratos inteligentes, las vulnerabilidades más frecuentes, los ataques reales más representativos y las herramientas actuales de análisis. Finalmente, se identifican las limitaciones del estado del arte que justifican el desarrollo de una librería en Python orientada a la integración y correlación de resultados de seguridad.

## 2.1. Fundamentos blockchain y contratos inteligentes

La tecnología **_blockchain_** se define como un sistema de registro distribuido (_distributed ledger_) que permite almacenar y gestionar información de forma descentralizada, segura y resistente a manipulaciones, sin depender de una autoridad central de confianza. Este paradigma fue introducido por Satoshi Nakamoto en 2008, en el contexto del diseño de Bitcoin, donde se propone un sistema de dinero electrónico _peer-to-peer_ basado en un libro mayor compartido entre múltiples nodos de la red. [1]

En una blockchain, las transacciones se agrupan en estructuras denominadas **bloques**, que se enlazan secuencialmente mediante **funciones hash criptográficas**. Cada bloque contiene, entre otros elementos, un conjunto de transacciones validadas, una marca temporal y el hash del bloque anterior. Este encadenamiento garantiza la integridad del sistema, ya que cualquier modificación en un bloque previamente confirmado alteraría su hash, rompiendo la continuidad de la cadena y permitiendo detectar manipulaciones de forma inmediata. [2]

Figura 1. Cadena genérica de bloques

![](data:image/png;base64,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)

Fuente: Blockchain Technology Overview, NISTIR 8202.

Adicionalmente, blockchain emplea criptografía asimétrica para asegurar la autenticidad e integridad de las transacciones. Cada participante dispone de un par de claves criptográficas (clave pública y clave privada), donde la clave privada se utiliza para firmar digitalmente las transacciones, y la clave pública permite a otros nodos verificar su validez. Este mecanismo elimina la necesidad de intermediarios de confianza, trasladando la verificación al propio sistema distribuido. [2]

### 2.1.1.  Tipos de redes blockchain

Las redes blockchain pueden clasificarse en función de su modelo de acceso y gobernanza, distinguiéndose principalmente entre redes públicas (_permissionless_) y redes privadas (_permissioned_).

Las **_blockchains_** _**permisionless**_ permiten la participación abierta de cualquier usuario, que puede leer el estado del _ledger_ y, dependiendo del protocolo de consenso, participar en la validación de bloques. Este modelo prioriza la descentralización, la transparencia y la resistencia a la censura. Ejemplos representativos incluyen Bitcoin y Ethereum.

Por otro lado, las **_blockchains_** _**permissioned**_ restringen el acceso a un conjunto predefinido de participantes autorizados. En este contexto, los nodos validadores son conocidos y controlados, lo que permite optimizar el rendimiento, reducir el coste computacional y facilitar el cumplimiento de requisitos regulatorios. Sin embargo, este modelo introduce un mayor grado de centralización. Un ejemplo ampliamente adoptado en entornos empresariales es Hyperledger Fabric.

En términos generales, las redes públicas priorizan la transparencia y la descentralización, mientras que las redes privadas favorecen la eficiencia operativa, el control y la privacidad, lo que explica su adopción en contextos corporativos. [2]

### 2.1.2.  Consenso entre nodos

Uno de los problemas fundamentales en sistemas distribuidos consiste en lograr que un conjunto de nodos alcance un acuerdo sobre el estado del sistema, incluso en presencia de fallos o comportamientos maliciosos. Este problema ha sido ampliamente estudiado en la literatura, destacando el trabajo de Leslie Lamport junto con Shostak y Pease, quienes formalizaron el consenso en entornos con fallos arbitrarios mediante el _Byzantine Generals Problem_, sentando las bases de la tolerancia a fallos bizantinos (_Byzantine Fault Tolerance_, BFT). [3]

En este contexto, un sistema tolerante a fallos bizantinos debe ser capaz de alcanzar consenso incluso cuando algunos nodos presentan comportamientos maliciosos o arbitrarios, como el envío de información falsa o la manipulación deliberada del protocolo. Este modelo resulta especialmente relevante en redes abiertas y sin permisos, como las blockchain públicas, donde no existe una relación de confianza previa entre los participantes.

No obstante, no todos los algoritmos de consenso contemplan este modelo adversarial. Protocolos clásicos como _Paxos Protocol_ están diseñados para entornos con fallos por parada (_crash faults_), en los que los nodos pueden fallar o dejar de responder, pero no actúan de forma maliciosa. Esta limitación los hace inadecuados para escenarios abiertos como blockchain, donde se asume la posible existencia de actores maliciosos. [4]

A partir de estos fundamentos, las redes blockchain han desarrollado mecanismos de consenso específicos que permiten mantener la coherencia del sistema en entornos descentralizados y potencialmente hostiles. [2]Entre los más relevantes destacan:

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

Cada uno de estos mecanismos implica distintos compromisos entre seguridad, descentralización y rendimiento, lo que en la literatura se describe frecuentemente como un conjunto de _trade-offs_ inherentes al diseño de sistemas blockchain, comúnmente denominado el “trilema de blockchain”. [5], [6]

Desde una perspectiva de ciberseguridad, la elección del protocolo de consenso no solo condiciona la arquitectura del sistema, sino también su superficie de ataque. En particular, estos compromisos influyen directamente en la viabilidad de vectores de explotación como ataques del 51%, censura de transacciones o manipulación del orden de ejecución (_front-running_), especialmente en entornos abiertos y sin permisos.

### 2.1.3.  Fundamentos de contratos inteligentes

Los **contratos inteligentes** (_smart contracts_) constituyen una extensión funcional de la tecnología blockchain que permite la ejecución de lógica programable de forma descentralizada. El concepto fue introducido por Nick Szabo en 1994, quien los definió como “un protocolo de transacción informatizado que ejecuta los términos de un contrato” [7]

En la actualidad, los contratos inteligentes se materializan como programas desplegados en una red blockchain que encapsulan tanto lógica como estado persistente. Su ejecución es llevada a cabo por los nodos de la red, los cuales deben alcanzar un resultado determinista e idéntico para garantizar la coherencia global del sistema. Este requisito impone restricciones relevantes en el diseño del software, especialmente en lo relativo al uso de fuentes externas de información o funciones no deterministas.

Cabe destacar que no todas las plataformas blockchain soportan contratos inteligentes. Redes como Bitcoin incorporan un lenguaje de scripting limitado, diseñado para priorizar la seguridad y la simplicidad, mientras que otras plataformas como Ethereum permiten la ejecución de código arbitrario, habilitando así el desarrollo de aplicaciones complejas sobre la blockchain. [8]

### 2.1.4. Ethereum Virtual Machine

La adopción generalizada de contratos inteligentes se consolidó con la aparición de Ethereum, que introduce un entorno de ejecución específico denominado **_Ethereum Virtual Machine_ (EVM)**. Esta máquina virtual permite la ejecución de código de propósito general dentro de un entorno distribuido y determinista.

El funcionamiento interno de Ethereum se describe formalmente en el _Yellow Paper_, elaborado por Gavin Wood, donde se definen:

- La arquitectura y semántica de la EVM
- El modelo de ejecución de contratos y transacciones
- El sistema de gas como mecanismo de control de recursos

La EVM es una máquina virtual basada en pila (_stack-based_), donde cada operación tiene un coste asociado en gas. Este mecanismo permite limitar el consumo de recursos computacionales y actúa como protección frente a ataques de denegación de servicio, al imponer un coste económico a la ejecución de operaciones complejas o potencialmente abusivas. [9]

### 2.1.5. Propiedades de los contratos inteligentes

Desde un punto de vista técnico, los contratos inteligentes presentan una serie de propiedades fundamentales[2]:

- **Determinismo**: la ejecución debe producir el mismo resultado en
  todos los nodos, garantizando la coherencia del sistema distribuido.
- **Inmutabilidad**: una vez desplegados, los contratos no pueden
  modificarse directamente, lo que dificulta la corrección de errores.
- **Transparencia**: en redes públicas, el código y el estado del
  contrato son accesibles, favoreciendo la auditabilidad.
- **Ejecución descentralizada**: no existe un punto único de control,
  eliminando dependencias de entidades centrales.

### 2.1.6. Limitaciones y riesgos

A pesar de sus ventajas, los contratos inteligentes presentan importantes desafíos desde el punto de vista de la ciberseguridad [2]:

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

Estas características hacen que los errores en contratos inteligentes puedan tener consecuencias críticas, como la pérdida irreversible de activos digitales. [2], [10]

### 2.1.7. Aplicaciones descentralizadas (DApps)

Sobre la base del modelo de ejecución, las propiedades y las limitaciones descritas, los contratos inteligentes permiten la construcción de aplicaciones descentralizadas (_Decentralized Applications_, DApps), que constituyen sistemas completos en los que la lógica de negocio se implementa parcial o totalmente mediante contratos inteligentes. [11]

A diferencia de las aplicaciones tradicionales basadas en arquitecturas cliente-servidor, las DApps distribuyen la lógica entre múltiples nodos de la red, eliminando intermediarios y reduciendo la dependencia de entidades centralizadas. Este cambio implica una redefinición del modelo de confianza, donde los usuarios depositan su confianza en el código ejecutado en la blockchain y en las garantías del protocolo subyacente.

Desde la perspectiva de la ciberseguridad, este paradigma introduce implicaciones relevantes. La transparencia del código facilita su auditoría, pero también permite a actores maliciosos analizarlo en busca de vulnerabilidades. Asimismo, la composición de múltiples contratos y la dependencia de servicios externos amplían la superficie de ataque, pudiendo dar lugar a vulnerabilidades complejas en sistemas interconectados, como ocurre en el ecosistema DeFi.

Además, la inmutabilidad de los contratos implica que los errores no pueden corregirse fácilmente tras su despliegue, lo que incrementa el impacto potencial de cualquier vulnerabilidad explotada. [12]

## 2.2. Finanzas Descentralizadas (DeFi): ecosistema y riesgo estructural

Las finanzas descentralizadas, conocidas por su acrónimo en inglés _DeFi_ (_Decentralized Finance_), constituyen un conjunto de aplicaciones y protocolos financieros construidos sobre redes blockchain públicas que permiten ofrecer diversos servicios financieros entre los que destacan: préstamos, intercambios de activos, emisión de derivados, gestión de rendimientos… sin la intervención de intermediarios centralizados como bancos, brokers o cámaras de compensación [13]. A diferencia del sistema financiero tradicional, en el que la confianza recae sobre instituciones reguladas y supervisadas por autoridades, en DeFi la lógica de negocio queda codificada íntegramente en contratos inteligentes desplegados en la cadena, accesibles públicamente y ejecutados de forma determinista por la red sin posibilidad de intervención posterior [13][14].

El origen del término suele situarse en torno a 2018, aunque el concepto tomó relevancia real a partir del fenómeno conocido como _DeFi Summer_ en 2020, cuando el valor total bloqueado (_Total Value Locked_, TVL) en protocolos de este tipo pasó de apenas 1.000 millones de dólares a superar los 15.000 millones en pocos meses[13]. En el pico del ciclo alcista de 2021, el TVL global llegó a superar los 180.000 millones de dólares, lo que convirtió al ecosistema DeFi en uno de los entornos de mayor concentración de activos digitales del mundo y, en consecuencia, en uno de los objetivos más atractivos para actores maliciosos [14].

La infraestructura de DeFi se organiza en torno a cuatro categorías de protocolos fundamentales [13]. Los _exchanges_ descentralizados (DEX) permiten el intercambio de activos sin custodia centralizada, utilizando modelos de _market maker_ automatizado (AMM) en los que la liquidez es aportada por los propios usuarios a través de fondos comunes. Los protocolos de préstamo y depósito, como Aave o Compound, permiten a los usuarios obtener crédito colateralizado o depositar activos para obtener rendimiento, con tipos de interés determinados algorítmicamente en función de la oferta y la demanda. Los protocolos de derivados y activos sintéticos, como Synthetix, permiten la exposición a precios de activos del mundo real sin necesidad de su custodia. Finalmente, los agregadores de rendimiento automatizan estrategias de inversión combinando múltiples protocolos en una única operación.

Todos estos protocolos comparten una característica importante desde el punto de vista de la seguridad: gestionan directamente activos económicos reales mediante contratos inteligentes inmutables o de difícil actualización, lo que convierte cualquier vulnerabilidad en un riesgo de pérdida irreversible de fondos [14].

## 2.3. Interoperabilidad blockchain: bridges y protocolos cross-chain

### 2.3.1.  El problema de las blockchains aisladas

El ecosistema blockchain no es un sistema unificado, sino un conjunto de redes independientes con arquitecturas, lenguajes de contrato, modelos de consenso y activos nativos distintos. Ethereum concentra la mayor parte de la liquidez DeFi, pero redes como BNB Chain, Solana, Avalanche, Polygon o Arbitrum cuentan con ecosistemas propios de considerable tamaño e importancia económica. Esta fragmentación responde en parte a la búsqueda de propiedades específicas (mayor rendimiento, menores costes de transacción o mayor privacidad) que ninguna cadena única ha logrado ofrecer de forma simultánea con suficiente madurez [15].

Sin embargo, la coexistencia de múltiples redes introduce un problema estructural: por diseño, una blockchain es un sistema cerrado que opera bajo sus propias reglas de consenso y no tiene capacidad para verificar de forma nativa el estado de otra cadena [15]. Un nodo de Ethereum no puede comprobar directamente si una transacción ha ocurrido en Solana ni si un activo ha sido bloqueado en BNB Chain. Esta limitación, conocida en la literatura como el problema de la comunicación entre _ledgers_ distribuidos, impide que los activos y la información fluyan libremente entre redes sin recurrir a mecanismos intermediarios [15][16]

Las consecuencias prácticas de esta fragmentación son significativas. La liquidez se encuentra dispersa entre múltiples cadenas, lo que encarece las operaciones para los usuarios y reduce la eficiencia del mercado. Los usuarios que desean aprovechar oportunidades en distintas redes se ven obligados a recurrir a _exchanges_ centralizados o a mecanismos de transferencia que introducen costes, demoras y, en muchos casos, riesgos adicionales. En respuesta a esta problemática, la industria ha desarrollado una categoría de protocolos conocidos como bridges o puentes cross-chain, cuya función es permitir la transferencia de activos e información entre blockchains heterogéneas [15][16].

Zamyatin et al. formalizan este problema en su trabajo seminal sobre comunicación entre ledgers distribuidos, estableciendo que cualquier protocolo de interoperabilidad debe garantizar propiedades de seguridad como la atomicidad (la transferencia ocurre por completo o no ocurre) y la consistencia (el estado de ambas cadenas refleja correctamente la operación realizada) [15]. Su análisis concluye que cumplir estas propiedades de forma simultánea en un entorno sin confianza requiere suposiciones criptográficas o de confianza que constituyen, precisamente, los puntos de fragilidad del sistema.

### 2.3.2. Tipos de bridges y arquitecturas

La literatura clasifica los bridges según dos dimensiones complementarias: el mecanismo de transferencia que utilizan y el modelo de confianza sobre el que se apoyan [15][16]. Esta clasificación es relevante no solo desde el punto de vista técnico, sino también desde la perspectiva de la seguridad, ya que distintos diseños implican distintas superficies de ataque y distintos supuestos de confianza.

Desde el punto de vista del mecanismo de transferencia, los modelos principales son cuatro.

El **modelo _Lock-and-Mint_**, el más extendido en la práctica, bloquea los activos en un contrato de custodia en la cadena de origen y acuña tokens representativos en la cadena de destino. Cuando el usuario desea recuperar sus activos originales, los tokens representativos son destruidos y el contrato de custodia libera los activos bloqueados. Este modelo es sencillo de implementar, pero introduce un riesgo de concentración: el contrato de custodia en la cadena de origen se convierte en un punto crítico que concentra los activos de todos los usuarios [16].

El **modelo _Burn-and-Mint_** elimina la necesidad de custodia centralizada destruyendo los tokens en la cadena de origen antes de acuñar equivalentes en la cadena de destino. Esto requiere que el token cuente con contratos de emisión desplegados en ambas cadenas con autoridad para quemar y acuñar. Los _Atomic Swaps_ permiten intercambios directos entre cadenas mediante contratos de tiempo bloqueado (_Hash Time-Locked Contracts_, HTLC), que garantizan que la transferencia es atómica sin necesidad de custodia de terceros, aunque con limitaciones de liquidez y compatibilidad entre cadenas [15]. Finalmente, las _Liquidity Networks_ utilizan pools de liquidez pre-fondeados en cada cadena para facilitar las transferencias, reduciendo los tiempos de espera a costa de requerir capital inmovilizado en ambos extremos.

Desde el punto de vista del modelo de confianza, Belchior et al. establecen una taxonomía en cuatro niveles [16]. Los bridges custodiales o centralizados confían en una única entidad que custodia los activos bloqueados y autoriza las acuñaciones en la cadena destino, lo que los hace rápidos y sencillos pero equivalentes en términos de riesgo a un _exchange_ centralizado. Los bridges basados en _multisig_ distribuyen la autorización entre un conjunto de validadores, requiriendo que un umbral mínimo de ellos firme cada operación; su seguridad depende directamente del número de validadores, su independencia y la protección de sus claves privadas. Los bridges con _light clients_ eliminan la necesidad de confiar en validadores externos verificando pruebas criptográficas del estado de la cadena de origen directamente en el contrato de la cadena de destino, lo que los hace más seguros, pero también más complejos y costosos en términos de gas. Los _ZK-bridges_, el estado del arte actual, utilizan pruebas de conocimiento cero para demostrar matemáticamente la corrección de las _transacciones cross-chain_ sin revelar información adicional, ofreciendo garantías de seguridad muy superiores, si bien su adopción generalizada aún está limitada por la complejidad computacional de generación de pruebas [16].

### 2.3.3. Componentes técnicos de un bridge

Con independencia del modelo concreto adoptado, los bridges comparten una serie de componentes técnicos cuya correcta implementación es determinante para su seguridad [15][16].

Los contratos inteligentes de bloqueo y acuñación constituyen el núcleo del bridge en la capa _on-chain_. En la cadena de origen, un contrato recibe y custodia los activos del usuario, emitiendo un evento que sirve como prueba de la operación. En la cadena de destino, un segundo contrato recibe la prueba verificada y acuña los activos representativos. La lógica de estos contratos debe implementar correctamente las comprobaciones de autorización, los mecanismos de verificación de pruebas y las condiciones de reversión ante situaciones anómalas [15].

Los validadores o _relayers_ son los componentes que operan fuera de la cadena y cuya función es detectar eventos en la cadena de origen, construir las pruebas correspondientes y enviarlas al contrato de la cadena de destino. En _bridges multisig_, cada validador firma independientemente la prueba de la operación, y el contrato de destino verifica que se ha alcanzado el umbral de firmas requerido antes de ejecutar la acuñación. La seguridad de este componente depende en gran medida de la gestión de claves privadas de los validadores y de la distribución del conjunto validador [16].

Los sistemas de verificación de pruebas son el mecanismo mediante el cual el contrato de la cadena de destino comprueba que la operación declarada por el _relayer_ ha ocurrido realmente en la cadena de origen. Según la arquitectura del bridge, esta verificación puede basarse en la comprobación de un umbral de firmas de validadores autorizados, en la verificación de una prueba Merkle sobre el estado de la cadena de origen, o en la verificación de una prueba criptográfica de conocimiento cero. La corrección de este componente es crítica: un fallo en la lógica de verificación puede permitir a un atacante fabricar pruebas falsas y acuñar activos sin respaldo [15].

Finalmente, los mecanismos de seguridad complementarios incluyen sistemas de límites de transferencia por período de tiempo, funciones de pausa de emergencia, esquemas de _timelock_ para operaciones de actualización del protocolo y sistemas de monitorización _on-chain_. Aunque estos mecanismos no eliminan las vulnerabilidades subyacentes, pueden limitar el impacto de un exploit al reducir la ventana de tiempo durante la cual un atacante puede extraer fondos antes de que el protocolo sea pausado [16].

La combinación de todos estos componentes hace que los bridges sean sistemas de complejidad técnica considerablemente superior a la de un contrato DeFi convencional. Operan simultáneamente en múltiples entornos de ejecución heterogéneos, dependen de componentes _off-chain_ con sus propios vectores de compromiso, y gestionan volúmenes de activos que los convierten en objetivos de alto valor económico. Esta combinación de complejidad, heterogeneidad y concentración de activos explica por qué los bridges han concentrado algunas de las pérdidas más significativas de la historia del ecosistema blockchain, y por qué su análisis de seguridad plantea desafíos específicos que trascienden las capacidades de las herramientas de análisis de contratos inteligentes actualmente disponibles [17]. Las vulnerabilidades concretas que afectan a estos sistemas, así como los ataques reales que las han materializado, se analizan en los apartados siguientes de este estado del arte.

## 2.4. Herramientas de Análisis

### 2.4.1. Slither

#### 2.4.1.1. Descripción y características principales

**Slither** es un framework de análisis estático de código abierto diseñado específicamente para la evaluación de seguridad de contratos inteligentes desarrollados en **Solidity** y **Vyper**. En la actualidad, se posiciona como una de las herramientas más robustas y ampliamente adoptadas tanto en el ámbito académico como en la industria de la auditoría de protocolos descentralizados.

Desarrollado por la firma de seguridad Trail of Bits, su presentación formal tuvo lugar en 2019 a través del artículo de investigación Slither: A Static Analysis Framework For Smart Contracts [18],  cuyos autores son Josselin Feist, Gustavo Grieco y Alex Groce

Arquitectura y Funcionamiento

El núcleo de Slither está implementado en **Python** y su principal ventaja competitiva reside en su flujo de análisis. A diferencia de otras herramientas que operan directamente sobre el bytecode de la Ethereum Virtual Machine (EVM), Slither recupera el Árbol de Sintaxis Abstracta (AST) de los contratos y lo traduce a una representación intermedia propia denominada **SlithIR**.

Esta representación, basada en _Static Single Assignment_ (SSA), permite realizar análisis de flujo de datos y de control con una precisión elevada, facilitando la detección de vulnerabilidades complejas que los _linters_ convencionales suelen omitir.

#### 2.4.1.2. Capacidades y Características Principales

De acuerdo con sus especificaciones técnicas y su repositorio oficial [19], Slither ofrece un conjunto de funcionalidades críticas para el desarrollo seguro:

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
	- Tiempo de ejecución promedio inferior a 1 segundo por contrato, lo que lo hace ideal para despliegues a gran escala.

#### 2.4.1.3. Impacto en la Seguridad de Contratos Inteligentes

La importancia de Slither radica en su equilibrio entre **velocidad y precisión**. Al operar sobre SlithIR, la herramienta puede realizar análisis semánticos profundos sin la carga computacional que requieren los motores de ejecución simbólica, permitiendo una validación constante durante la fase de desarrollo del contrato.

#### 2.4.1.4. Limitaciones de Slither

A pesar de su eficiencia, Slither presenta limitaciones propias del análisis estático que deben ser consideradas. La herramienta no modela interacciones complejas entre múltiples contratos de forma dinámica, lo que le impide detectar vulnerabilidades de lógica económica, como la manipulación de oráculos o ataques de _flash loans_. Asimismo, en entornos de código con alta complejidad, múltiples niveles de herencia o uso de ensamblador (_inline assembly_), Slither suele generar una tasa elevada de falsos positivos. Esto requiere que el auditor realice una validación manual exhaustiva para distinguir las vulnerabilidades reales de las falsas alarmas detectadas por el software.

#### 2.4.1.5. Empresas y organizaciones que lo utilizan

En el sector de la seguridad blockchain, Slither se ha consolidado como una herramienta de referencia. Es utilizada de manera sistemática por firmas de auditoría líderes como **ConsenSys Diligence****,** **Sigma Prime** y **OpenZeppelin** para realizar el triaje inicial de los contratos. Además, su integración en flujos de trabajo de integración continua (CI/CD) es un estándar en los protocolos DeFi más relevantes, entre los que destacan **Aave****,** **Uniswap****,** **Yearn Finance** y **Compound**. Estas organizaciones emplean el _framework_ para automatizar el escaneo de seguridad en cada actualización de sus repositorios antes del despliegue definitivo en la red.[20], [21], [22]

### 2.4.2. Mythril — Ejecución Simbólica (ConsenSys)

#### 2.4.2.1. Descripción y características principales

Mythril es una herramienta de seguridad de código abierto diseñada para el análisis profundo de contratos inteligentes que se ejecutan en la Ethereum Virtual Machine (EVM). A diferencia de los analizadores estáticos convencionales, Mythril se categoriza como un motor de ejecución simbólica, capaz de evaluar la seguridad de los contratos tanto a nivel de código fuente (Solidity) como directamente sobre el bytecode de la EVM [23]. Su propósito principal es identificar estados del contrato que podrían conducir a vulnerabilidades críticas mediante la exploración de rutas de ejecución que no son evidentes mediante la simple lectura del código.[24]

#### 2.4.2.2. Arquitectura y Funcionamiento

El núcleo de Mythril se basa en la **ejecución simbólica con resolución SMT (_Satisfiability Modulo Theories_)****.** Su funcionamiento se puede desglosar en tres fases técnicas:

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

#### 2.4.2.3. Capacidades y Características Principales

En cuanto a su potencial técnico, Mythril sobresale por su capacidad para identificar fallos lógicos de alta complejidad que están estrechamente vinculados a la manipulación del estado de la cadena de bloques.

Entre sus funciones más destacadas se encuentra la detección especializada de vulnerabilidades críticas, tales como la reentrancia clásica, el uso indebido de la instrucción DELEGATECALL, las dependencias de _timestamp_ y los desbordamientos de enteros (_integer overflows/underflows_), estos últimos especialmente relevantes en contratos desarrollados con versiones de Solidity anteriores a la 0.8.

Asimismo, la herramienta ofrece una versatilidad notable mediante su funcionalidad de análisis de Mainnet, la cual permite recuperar el bytecode directamente desde un nodo de Ethereum; esto facilita la auditoría de contratos que ya han sido desplegados incluso si el código fuente original no está disponible.

Finalmente, una de sus características más valoradas por los auditores es la generación detallada de trazas de ejecución, ya que el sistema no se limita a reportar la existencia de un error, sino que reconstruye la secuencia exacta de transacciones necesaria para recrear el exploit y validar la vulnerabilidad.

#### 2.4.2.4. Limitaciones Técnicas

A pesar de su robustez, Mythril enfrenta desafíos significativos derivados de la naturaleza de la ejecución simbólica. El obstáculo más crítico es la denominada explosión de caminos (_path explosion_), un fenómeno que ocurre en contratos con estructuras de control muy ramificadas o bucles complejos. En estos escenarios, el número de estados posibles aumenta de forma exponencial, lo que deriva frecuentemente en un consumo excesivo de memoria o en la interrupción del proceso por tiempo de espera (_timeout_) antes de completar el análisis.[25]

A esta limitación estructural se suma una tasa considerable de falsos positivos, la cual se estima en estudios independientes entre el 45% y el 52%. Esta imprecisión suele deberse a que la herramienta, para mantener la viabilidad del cálculo, simplifica ciertos aspectos del entorno de la blockchain, como el estado de contratos externos o variables ambientales complejas, lo que puede llevar a reportar vulnerabilidades que no son explotables en un entorno real.[26]

Finalmente, el rendimiento operativo de Mythril es notablemente inferior al de los analizadores estáticos como Slither. Debido a la carga computacional que requiere la resolución de fórmulas matemáticas mediante SMT, los tiempos de ejecución oscilan entre los 5 y 300 segundos por contrato. Esta demora depende directamente de la profundidad de exploración configurada, lo que lo hace menos ágil para procesos de integración continua que requieren una respuesta inmediata.

#### 2.4.2.5. Ecosistema y Adopción

En la actualidad, Mythril se consolida como un pilar fundamental dentro de la industria de la seguridad blockchain. Su relevancia técnica y trayectoria lo han posicionado como el motor central de **MythX**, la plataforma de análisis de seguridad profesional bajo modelo SaaS desarrollada por ConsenSys. Esta integración permite a los desarrolladores acceder a las capacidades de Mythril directamente desde sus entornos de trabajo habituales.

Asimismo, la herramienta se ha convertido en un estándar dentro de los flujos de trabajo de **auditoría profesional**. Firmas de prestigio internacional, tales como **ConsenSys Diligence** y **Halborn**, emplean Mythril de forma sistemática para complementar sus revisiones manuales, utilizando su capacidad de exploración de estados para detectar errores lógicos que podrían pasar desapercibidos en una lectura convencional del código.

Más allá del sector comercial, Mythril posee una fuerte presencia en la **comunidad académica**. Su naturaleza de código abierto y su arquitectura basada en el _solver_ Z3 lo convierten en una base tecnológica recurrente para investigaciones avanzadas. Es utilizado frecuentemente en estudios sobre verificación formal y en el desarrollo de nuevos protocolos de seguridad destinados a proteger el ecosistema de las finanzas descentralizadas (DeFi) [24], [25].

### 2.4.3. Echidna — Fuzzing Basado en Propiedades (Trail of Bits)

#### 2.4.3.1. Descripción y características principales

Echidna es una herramienta de código abierto desarrollada por Trail of Bits, diseñada específicamente para el análisis de seguridad de contratos inteligentes en Ethereum mediante la técnica de _fuzzing_ basado en propiedades. A diferencia de las pruebas unitarias tradicionales, que se limitan a verificar resultados ante entradas específicas, este marco de trabajo busca falsar invariantes o predicados definidos por el usuario, permitiendo identificar fallos lógicos complejos que suelen pasar desapercibidos en procesos de testeo convencionales. Implementado en Haskell, el programa destaca por su facilidad de uso, ya que no requiere configuraciones complejas ni el despliegue previo de los contratos en una red local.[27]

#### 2.4.3.2. Arquitectura y Funcionamiento

El funcionamiento de Echidna se fundamenta en la generación de campañas de _fuzzing_ basadas en gramática, utilizando el ABI (_Application Binary Interface_) del contrato para interactuar con él. El flujo de trabajo comienza cuando el desarrollador define propiedades de seguridad en el código Solidity, normalmente funciones con el prefijo `echidna_` que deben devolver siempre un valor booleano verdadero. A partir de estas definiciones, la herramienta ejecuta millones de secuencias de transacciones aleatorias y sofisticadas con el objetivo de alcanzar un estado del contrato que rompa dichas reglas.[28]

#### 2.4.3.3. Capacidades y Características Principales

Una de las capacidades más potentes de este fuzzer es su capacidad de reducción de casos de prueba. Cuando Echidna detecta una violación de una propiedad o una aserción de Solidity, el sistema realiza una simplificación automática para reportar la secuencia mínima de transacciones necesaria para reproducir el error. Esta eficiencia en la detección y reporte ha quedado demostrada en entornos reales de producción; ya en la fecha de publicación de su _paper_ original, la herramienta había sido validada con éxito en más de diez auditorías de seguridad de gran escala, consolidándose como un estándar en el ecosistema de seguridad de _smart contracts_.[27]

#### 2.4.3.4. Limitaciones Técnicas

A pesar de su eficacia, Echidna presenta restricciones técnicas inherentes a su metodología de prueba. En primer lugar, la calidad del análisis depende de la calidad de las propiedades definidas por el usuario; si el desarrollador no define correctamente los invariantes, Echidna no podrá identificar fallos de lógica específicos [29].

Por otro lado, la herramienta puede enfrentar problemas de rendimiento en contratos con funciones extremadamente costosas en términos de gas o con estructuras de datos ineficientes, lo que ralentiza la generación de transacciones [28].

Asimismo, aunque es excelente para detectar errores lógicos, tiene dificultades para analizar contratos que dependen de condiciones externas muy específicas de la red que no pueden ser fácilmente simuladas en su entorno local de pruebas[29].

### 2.4.3.5. Ecosistema y Adopción

Debido a su eficacia demostrada, Echidna se ha convertido en una herramienta estándar en la industria:

·      **Trail of Bits:** Como creadores de la herramienta, la utilizan en todas sus auditorías de alto perfil para protocolos DeFi [28].

·      **Auditores Profesionales:** Firmas de ciberseguridad blockchain emplean Echidna para validar la robustez de protocolos antes de su despliegue en la red principal [29].

·      **Equipos de Desarrollo:** Proyectos de infraestructura y finanzas descentralizadas integran Echidna en sus tuberías de **Integración Continua (CI/CD)** para garantizar que cada actualización de código mantenga los invariantes de seguridad [27].

## 2.5. Vulnerabilidades de seguridad en contratos inteligentes de Ethereum

Los contratos inteligentes en Ethereum presentan un modelo de seguridad distinto al del software tradicional. Su ejecución es pública, el código es accesible y cualquier error puede ser analizado y explotado por actores con incentivos económicos directos. Además, la inmutabilidad dificulta la corrección de fallos una vez desplegado el contrato, y la interacción con otros contratos y servicios externos incrementa la superficie de ataque. [10], [30]

Por este motivo, una vulnerabilidad en Solidity no debe entenderse solo como un error de programación, sino como una debilidad explotable en un entorno adversarial. En la práctica, los problemas de seguridad no se limitan a fallos técnicos, sino que también incluyen errores de diseño y de lógica de negocio. [31]

Para su análisis, resulta útil agrupar las vulnerabilidades en cuatro categorías principales:

- Vulnerabilidades técnicas de ejecución
- Vulnerabilidades de control y privilegios
- Vulnerabilidades económicas y dependencia del entorno
- Errores lógicos de negocio

### 2.5.1. Vulnerabilidades técnicas de ejecución

Este grupo incluye errores directamente relacionados con la ejecución en la EVM y la implementación en Solidity.

Una de las más conocidas es la **reentrancy**, que ocurre cuando un contrato realiza una llamada externa antes de actualizar su estado interno. Esto permite que el contrato receptor vuelva a ejecutar la función vulnerable con un estado inconsistente. A pesar de que existen patrones de mitigación bien conocidos, sigue siendo una de las vulnerabilidades más relevantes en Ethereum. [32]

Otra categoría importante son los **problemas aritméticos**, como overflow y underflow. Aunque Solidity 0.8 introduce comprobaciones automáticas, estos errores siguen siendo relevantes en contratos antiguos, en bloques unchecked o en cálculos financieros incorrectos.

También destacan las **llamadas externas inseguras**, ya que cualquier call transfiere el control de ejecución a otro contrato. Esto puede provocar comportamientos inesperados o ejecución de lógica maliciosa. En esta línea, el uso de delegatecall es especialmente crítico, ya que ejecuta código externo sobre el almacenamiento del contrato llamador, pudiendo comprometer completamente su estado.  [30]

Por último, los **ataques de denegación de servicio (DoS)** son frecuentes en este entorno. No buscan tumbar el sistema, sino bloquear funciones críticas, por ejemplo, mediante bucles no acotados o reversiones provocadas por contratos externos. [30]

### 2.5.2. Vulnerabilidades de control y privilegios

Muchas vulnerabilidades reales no se deben a errores técnicos complejos, sino a problemas en el control de acceso.

Esto incluye funciones sensibles sin restricciones, roles mal definidos o privilegios excesivos. Un error típico es permitir que cualquier usuario ejecute funciones críticas como transferencias de fondos o cambios de configuración. [33]

Un caso especialmente problemático es el uso de tx.origin para autenticación. Este valor representa el origen externo de la transacción, no el llamador inmediato, lo que permite ataques mediante contratos intermedios.

También son relevantes los problemas en contratos upgradeables, especialmente los relacionados con inicializadores. Si una función initialize no está correctamente protegida, un atacante puede ejecutarla y asumir el control del contrato. [34]

### 2.5.3. Vulnerabilidades económicas y dependencia del entorno

En muchos casos, el problema no está en el código en sí, sino en cómo interactúa el contrato con su entorno.

El ejemplo más claro es el **front-running**, donde un atacante observa transacciones en la mempool y envía otras con mayor prioridad para ejecutarse antes. Este fenómeno forma parte del problema más amplio del **MEV (Maximal Extractable Value)** y afecta especialmente a aplicaciones DeFi. [35]

Otro riesgo importante es la **manipulación de oráculos**. Si un contrato depende de precios externos que pueden alterarse temporalmente, un atacante puede aprovechar esa situación para obtener beneficios indebidos, por ejemplo, en protocolos de préstamo. [33]

En esta categoría también se incluyen los problemas de **aleatoriedad insegura** y el uso de block.timestamp como fuente de decisiones críticas. Estas variables no son completamente fiables ni impredecibles, por lo que pueden ser manipuladas o anticipadas en determinados escenarios.

### 2.5.4. Errores lógicos de negocio

Los errores más difíciles de detectar son los relacionados con la lógica del contrato.

En estos casos, el código puede ser correcto desde el punto de vista técnico, pero implementar una lógica incorrecta. Esto incluye errores en cálculos de balances, distribución de recompensas, gestión de estados o validación de condiciones. [31]

Este tipo de vulnerabilidades es especialmente relevante porque suele escapar a las herramientas automáticas. Además, muchos ataques reales combinan errores lógicos con otros factores, como manipulación de precios o condiciones de ejecución. [35]

### 2.5.5. Conclusión

En conjunto, la seguridad en contratos inteligentes no puede abordarse únicamente mediante la detección de patrones conocidos. Aunque vulnerabilidades como reentrancy o overflow siguen siendo relevantes, los problemas más complejos suelen estar relacionados con el diseño del sistema, la interacción con otros componentes y la lógica de negocio.

Esto implica que una auditoría efectiva debe analizar no solo el código, sino también su comportamiento, sus dependencias y los incentivos que lo rodean.

  

## 2.6. Ataques Reales

El estudio de incidentes reales constituye una fuente de conocimiento imprescindible en el ámbito de la seguridad de contratos inteligentes. A diferencia de los entornos de prueba, los ataques producidos en redes de producción demuestran cómo las vulnerabilidades teóricas se traducen en pérdidas económicas concretas e irreversibles.

En esta sección se analizan cuatro casos históricos representativos, seleccionados por su relevancia técnica y su correspondencia directa con cada una de las categorías de vulnerabilidades descritas en la sección anterior (4.4. Vulnerabilidades de seguridad en contratos inteligentes de Ethereum).

### 2.6.1. Vulnerabilidad técnica de ejecución: The DAO (2016)

El ataque contra The DAO, producido en junio de 2016, representa el caso más paradigmático de explotación de una vulnerabilidad de _reentrancy_ en la historia de Ethereum [36]. The DAO era un fondo de inversión descentralizado desplegado sobre Ethereum que había recaudado aproximadamente 150 millones de dólares en ETH procedentes de más de once mil participantes, convirtiéndose en uno de los mayores proyectos de financiación colectiva hasta ese momento [37].

La vulnerabilidad residía en la función withdraw() del contrato. El flujo de ejecución enviaba los fondos en ETH al destinatario antes de actualizar el balance interno correspondiente. Esta secuencia incorrecta permitió a un atacante desplegar un contrato receptor cuya función de _fallback_ re-invocaba withdraw() de forma recursiva, extrayendo fondos de manera repetida mientras el saldo del contrato permanecía sin modificar. El ataque se ejecutó en múltiples iteraciones dentro de una misma cadena de llamadas, drenando aproximadamente 3,6 millones de ETH [38].

Las consecuencias del incidente trascendieron lo puramente económico. La comunidad de Ethereum debatió durante semanas sobre cómo dar respuesta al ataque, dado el carácter inmutable del protocolo. Finalmente, se ejecutó un _hard fork_ en el bloque 1.920.000, el 20 de julio de 2016, que revirtió el estado de la cadena para recuperar los fondos. Una fracción de la comunidad rechazó esta intervención por considerarla contraria a los principios de inmutabilidad de la tecnología blockchain, lo que dio lugar a la bifurcación conocida como Ethereum Classic [37].

Este caso puso de manifiesto que el patrón de diseño correcto para gestionar transferencias es el denominado _checks-effects-interactions_: primero verificar condiciones, después actualizar el estado del contrato y, por último, realizar cualquier llamada externa. Su incumplimiento en The DAO, a pesar de la aparente sencillez del principio, resultó en pérdidas valoradas en torno a 60 millones de dólares al precio del momento [36].

### 2.6.2. Vulnerabilidad de control y privilegios: Poly Network (2021)

El ataque a Poly Network, ocurrido el 10 de agosto de 2021, ilustra con especial claridad las consecuencias de un control de acceso deficiente en contratos que gestionan operaciones críticas de alto valor [39]. Poly Network es un protocolo de interoperabilidad _cross-chain_ que conecta diversas redes blockchain, lo que amplía considerablemente su superficie de ataque.

El vector de explotación se basó en una ausencia de restricciones en la cadena de llamadas entre contratos del protocolo. La función verifyHeaderAndExecuteTx(), presente en el contrato EthCrossChainManager, permitía invocar internamente la función PutCurEpochConPubKeyBytes() del contrato EthCrossChainData, encargada de actualizar la clave pública del grupo de _keepers_ con permisos para ejecutar transacciones _cross-chain_. Al no existir ninguna comprobación que restringiese qué direcciones podían realizar esta invocación de forma indirecta, el atacante fue capaz de sustituir los _keepers_ legítimos por una dirección bajo su propio control.

La operación se replicó de forma simultánea en tres redes: Ethereum, BNB Chain y Polygon; lo que supuso un control inmediato sobre la práctica totalidad de los fondos bloqueados en el protocolo, con un valor estimado de 611 millones de dólares, convirtiéndose en el mayor robo de la historia del ecosistema DeFi hasta esa fecha.

El desenlace del incidente fue inusual: el atacante devolvió la totalidad de los fondos en los días posteriores, argumentando haber actuado con el propósito de demostrar la vulnerabilidad. No obstante, el caso evidencia que errores de diseño en el modelo de permisos (independientemente de su recuperabilidad) pueden comprometer completamente la integridad de un protocolo. Una correcta implementación de control de acceso, mediante modificadores de autorización explícitos y separación de privilegios entre contratos, habría impedido la escalada de permisos aprovechada en este ataque [40].

### 2.6.3. Vulnerabilidad económica y dependencia del entorno: bZx (2020)

Los ataques contra el protocolo bZx, producidos en febrero de 2020, constituyen uno de los primeros ejemplos documentados de explotación combinada de _flash loans_ y manipulación de oráculos de precio a escala en el ecosistema DeFi. Su relevancia radica no solo en las pérdidas económicas, sino en haber demostrado que la composabilidad de los protocolos DeFi puede convertirse en un vector de ataque cuando los componentes individuales no contemplan escenarios de manipulación externa [41].

En el primero de los dos incidentes, acaecido el 14 de febrero de 2020, el atacante obtuvo un préstamo flash de 10.000 ETH a través del protocolo dYdX sin necesidad de aportar colateral alguno. Con una parte de estos fondos abrió simultáneamente una posición corta apalancada sobre el par WBTC/ETH en bZx y utilizó el volumen restante para adquirir WBTC en Uniswap, manipulando artificialmente el precio de mercado del par en ese pool. El protocolo bZx, al depender de Uniswap como fuente de precios en tiempo real, calculó incorrectamente la valoración de la posición del atacante, quien la cerró obteniendo un beneficio aproximado de 350.000 dólares una vez devuelto el préstamo flash, todo dentro de una única transacción [42].

El segundo ataque, cuatro días después, siguió una mecánica similar pero orientada a la manipulación del precio del token sUSD en Kyber Network. Al inflar artificialmente su cotización, el atacante logró depositar colateral sobrevalorado en bZx y extraer en préstamo un volumen de activos muy superior al que le habría correspondido según condiciones de mercado normales [42].

Ambos ataques pusieron de manifiesto que la seguridad de un protocolo DeFi no puede analizarse de forma aislada: la dependencia de precios obtenidos de fuentes únicas y manipulables en tiempo real constituye una vulnerabilidad estructural. La adopción de oráculos descentralizados con agregación de múltiples fuentes de precio (como los proporcionados por protocolos del tipo Chainlink) y el uso de precios promediados en el tiempo (TWAP, _Time-Weighted Average Price_) son las principales contramedidas frente a este patrón de ataque.

  

### 2.6.4. Error lógico de negocio: Euler Finance (2023)

El ataque a Euler Finance, ejecutado el 13 de marzo de 2023, representa un ejemplo de elevada complejidad técnica dentro de la categoría de errores lógicos, precisamente porque la vulnerabilidad no residía en un patrón de codificación inseguro clásico, sino en una interacción no prevista entre mecanismos financieros del propio protocolo [43].

Euler Finance era un protocolo de préstamos descentralizado en Ethereum que introducía el concepto de _sub-cuentas_ para gestionar posiciones de colateral y deuda de forma independiente. La vulnerabilidad se encontraba en la función donateToReserves(), incorporada en una actualización anterior. Esta función permitía a un usuario transferir sus propios activos a las reservas del protocolo, pero no verificaba que dicha operación no dejase la cuenta del donante en un estado de insolvencia. En condiciones normales, esta situación habría sido detectada por el sistema de liquidación, pero el atacante aprovechó el mecanismo de autoliquidación del protocolo de una forma no contemplada en su diseño [44].

El flujo del ataque comenzó con la obtención de un préstamo flash de 30 millones de DAI desde el protocolo Aave. Con estos fondos, el atacante depositó colateral en Euler y, mediante operaciones de apalancamiento repetidas, construyó posiciones de aproximadamente 195 millones de eDAI (depósitos) y 200 millones de dDAI (deuda). A continuación, utilizó donateToReserves() para crear intencionalmente una posición insolvente y acto seguido activó la autoliquidación. El sistema de Euler, al calcular el bonus de liquidación sobre una posición de ese tamaño, transfirió al atacante los fondos de las reservas del protocolo en una cuantía muy superior a la deuda original [45].

La pérdida total ascendió a aproximadamente 197 millones de dólares. Sin embargo, el atacante devolvió la práctica totalidad de los fondos semanas después, tras una negociación directa con el equipo de Euler mediante mensajes publicados en la cadena de bloques. El incidente ilustra cómo la ausencia de validaciones sobre invariantes de negocio (en este caso, que ninguna operación debería permitir dejar una cuenta en estado de insolvencia) puede generar vulnerabilidades que escapan tanto a la revisión manual del código como a las herramientas de análisis estático-convencionales [44].

## 2.7. Síntesis y limitaciones del estado del arte

El análisis realizado muestra que el ecosistema de contratos inteligentes compatibles con la Ethereum Virtual Machine (EVM) concentra actualmente la mayor parte de herramientas, investigaciones y estándares relacionados con la seguridad en blockchain. Solidity se ha consolidado como el lenguaje dominante en el desarrollo de aplicaciones descentralizadas y protocolos DeFi, lo que ha favorecido la aparición de múltiples herramientas especializadas para el análisis de vulnerabilidades.

No obstante, el estado del arte también evidencia limitaciones relevantes. Herramientas como Slither, Mythril o Echidna utilizan enfoques distintos y generan resultados heterogéneos, dificultando la correlación de hallazgos y aumentando la necesidad de validación manual por parte de auditores especializados. Asimismo, muchas soluciones presentan dificultades para priorizar riesgos o contextualizar el impacto real de las vulnerabilidades detectadas.

Por otro lado, gran parte de las vulnerabilidades analizadas dependen principalmente del modelo de ejecución de la EVM y del diseño de los contratos inteligentes, siendo extrapolables a distintas redes compatibles como Ethereum, BNB Smart Chain, Polygon o Arbitrum. Por este motivo, el presente trabajo utilizará BNB Smart Chain Testnet como entorno de pruebas, aprovechando su compatibilidad con Solidity y la reducción de costes durante el desarrollo experimental.

En conjunto, estas limitaciones justifican la necesidad de desarrollar soluciones que permitan integrar múltiples herramientas de análisis, normalizar resultados y facilitar una interpretación más estructurada de los hallazgos de seguridad en contratos inteligentes.



\newpage


# 3. Objetivos concretos y metodología de trabajo
## 3.1. Objetivo general

El objetivo general del presente Trabajo Fin de Máster consiste en diseñar, implementar y evaluar una librería en Python orientada al análisis de seguridad de contratos inteligentes compatibles con la Ethereum Virtual Machine (EVM), capaz de integrar y correlacionar resultados procedentes de distintas herramientas de auditoría.

La propuesta busca facilitar el análisis de vulnerabilidades en contratos desarrollados en Solidity mediante un enfoque modular que permita unificar resultados heterogéneos y mejorar la interpretación de los hallazgos detectados.

## 3.2. Objetivos específicos

Para alcanzar el objetivo general se plantean los siguientes objetivos específicos:

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

## 3.3. Metodología del trabajo

Con el fin de alcanzar los objetivos planteados, el desarrollo del trabajo se estructuró en varias fases que combinaron tanto el análisis teórico del problema como la implementación práctica de la solución propuesta.

En una primera fase se realizó un estudio del estado del arte relacionado con blockchain, contratos inteligentes, vulnerabilidades en Solidity y técnicas de auditoría de seguridad. Asimismo, se analizaron distintas herramientas existentes para identificar sus capacidades, limitaciones y posibilidades de integración.

Posteriormente, se definió la arquitectura de la librería, estableciendo los módulos necesarios para la ejecución de herramientas externas, el procesamiento de resultados y la generación de informes. Durante esta etapa se priorizó un diseño modular y extensible que facilitase futuras ampliaciones y la incorporación de nuevos mecanismos de análisis.

A continuación, se llevó a cabo la implementación de la solución utilizando Python como lenguaje principal. La librería desarrollada integró herramientas externas de análisis y permitió automatizar el procesamiento, normalización y correlación de los resultados obtenidos.

Finalmente, se realizó una evaluación experimental utilizando contratos inteligentes vulnerables y casos reales obtenidos de repositorios públicos. Los resultados obtenidos permitieron analizar el comportamiento de la solución propuesta y valorar su utilidad como apoyo al análisis de seguridad de contratos inteligentes compatibles con la Ethereum Virtual Machine (EVM).


\newpage


# 4. Desarrollo de la solución propuesta

Una vez estudiadas las principales vulnerabilidades presentes en los contratos inteligentes y analizadas las herramientas existentes para su detección, en este capítulo se presenta la solución desarrollada para dar respuesta a los objetivos planteados en el presente Trabajo Fin de Máster.

La propuesta realizada, denominada **EVMAudit**, consiste en una librería desarrollada en Python orientada al análisis de seguridad de contratos inteligentes compatibles con la Ethereum Virtual Machine (EVM). La herramienta integra diferentes técnicas de análisis mediante la ejecución combinada de Slither, Mythril y Echidna, con el objetivo de aprovechar las capacidades específicas de cada una de ellas y proporcionar una visión más completa de las vulnerabilidades detectadas.

Con el fin de favorecer la mantenibilidad y la extensibilidad del sistema, se adoptó una arquitectura modular en la que cada componente implementa una responsabilidad específica dentro del proceso de análisis. De este modo, la solución permite automatizar la ejecución de las herramientas externas, procesar y correlacionar los resultados obtenidos y generar información adicional que facilite la validación posterior de las vulnerabilidades identificadas.

A lo largo de este capítulo se describen los requisitos que guiaron el desarrollo de la herramienta, la arquitectura diseñada y los distintos módulos implementados. Finalmente, se presenta la evaluación experimental realizada con el objetivo de analizar el comportamiento de la solución propuesta y valorar su utilidad como apoyo al proceso de auditoría de contratos inteligentes.

!TODO: referencia cruzada a la Sección 3.1 (objetivo general).

!TODO: referencia cruzada a la Sección 3.2 (objetivos específicos).

!TODO: referencia cruzada a la Sección 3.3 (metodología).


\newpage


# 4.1.Requisitos
## 4.1. Identificación de requisitos

A partir del análisis realizado durante el estudio del estado del arte y de las limitaciones observadas en las herramientas existentes, se definieron una serie de requisitos que sirvieron como base para el diseño e implementación de EVMAudit.

Los requisitos establecidos se clasifican en requisitos funcionales, requisitos no funcionales y requisitos de seguridad.

### 4.1.1. Requisitos funcionales

Los requisitos funcionales describen las capacidades que debe proporcionar la herramienta para satisfacer los objetivos del trabajo.

| ID    | Descripción                                                                                                                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| RF-01 | La herramienta debe permitir analizar contratos inteligentes desarrollados en Solidity.                                                    |
| RF-02 | La herramienta debe detectar automáticamente el nombre del contrato cuando no se especifique manualmente.                                  |
| RF-03 | La herramienta debe configurar automáticamente la versión del compilador Solidity necesaria para el análisis.                              |
| RF-04 | La herramienta debe ejecutar Slither como herramienta de análisis estático.                                                                |
| RF-05 | La herramienta debe ejecutar Mythril como herramienta de análisis mediante ejecución simbólica.                                            |
| RF-06 | La herramienta debe almacenar las salidas originales de las herramientas utilizadas.                                                       |
| RF-07 | La herramienta debe normalizar los resultados generados por Slither y Mythril a una estructura común.                                      |
| RF-08 | La herramienta debe asociar los hallazgos detectados con identificadores SWC.                                                              |
| RF-09 | La herramienta debe correlacionar hallazgos equivalentes procedentes de distintas herramientas.                                            |
| RF-10 | La herramienta debe indicar el nivel de confianza de los hallazgos en función de las herramientas que hayan detectado cada vulnerabilidad. |
| RF-11 | La herramienta debe generar automáticamente propiedades para su validación mediante Echidna.                                               |
| RF-12 | La herramienta debe ejecutar Echidna sobre los wrappers generados.                                                                         |
| RF-13 | La herramienta debe generar un informe final consolidado.                                                                                  |
| RF-14 | La herramienta debe conservar la trazabilidad de los resultados originales.                                                                |

### 4.1.2. Requisitos no funcionales

Los requisitos no funcionales definen las características de calidad que debe presentar la solución desarrollada.

| ID     | Descripción                                                                                    |
| ------ | ---------------------------------------------------------------------------------------------- |
| RNF-01 | La arquitectura de la herramienta debe ser modular.                                            |
| RNF-02 | La solución debe permitir la incorporación de nuevas herramientas en futuras versiones.        |
| RNF-03 | Los resultados intermedios deben almacenarse para garantizar la reproducibilidad del análisis. |
| RNF-04 | La solución debe presentar un bajo acoplamiento entre módulos.                                 |
| RNF-05 | La herramienta debe facilitar el mantenimiento y evolución futura del sistema.                 |
| RNF-06 | La lógica de análisis debe permanecer desacoplada de las interfaces de usuario.                |

### 4.1.3. Requisitos de seguridad

Debido a la naturaleza del trabajo, se definieron además una serie de requisitos orientados a mejorar la robustez del proceso de análisis.

| ID    | Descripción                                                                                    |
| ----- | ---------------------------------------------------------------------------------------------- |
| RS-01 | La herramienta debe detectar la ausencia de dependencias externas necesarias para el análisis. |
| RS-02 | La herramienta debe gestionar errores producidos por herramientas externas.                    |
| RS-03 | La herramienta debe controlar tiempos máximos de ejecución.                                    |
| RS-04 | La herramienta debe preservar las evidencias originales obtenidas durante el análisis.         |
| RS-05 | La herramienta debe permitir reproducir los resultados obtenidos.                              |

!TODO: insertar tabla definitiva con formato Word.

!TODO: referencia cruzada a las herramientas descritas en la Sección 2.X.

!TODO: referencia cruzada a las vulnerabilidades descritas en la Sección 2.X.



\newpage


# 4.2.Arquitectura
## 4.2. Arquitectura general de EVMAudit

Con el objetivo de satisfacer los requisitos definidos anteriormente, se diseñó una arquitectura modular que permitiese separar las distintas fases del proceso de análisis y facilitar la incorporación de nuevas funcionalidades en futuras versiones.

La arquitectura implementada divide el sistema en varios módulos especializados encargados de:

* ejecutar las herramientas externas
* procesar y normalizar los resultados obtenidos
* correlacionar vulnerabilidades equivalentes
* generar propiedades para Echidna
* ejecutar pruebas de fuzzing
* construir el informe final.

Esta separación de responsabilidades permite reducir el acoplamiento entre componentes y facilita la mantenibilidad del sistema.

### 4.2.1. Pipeline de análisis

El flujo general seguido por EVMAudit comienza con la recepción del contrato inteligente que se desea analizar. Posteriormente, la herramienta ejecuta Slither y Mythril para obtener resultados procedentes de análisis estático y ejecución simbólica.

Una vez finalizada esta fase, los resultados generados son normalizados y transformados a una estructura común. Posteriormente, se aplica el mecanismo de correlación implementado por EVMAudit con el objetivo de unificar vulnerabilidades equivalentes y aumentar la confianza de los hallazgos obtenidos.

A partir de los resultados correlacionados, se generan automáticamente propiedades para Echidna, construyendo un wrapper específico que permite realizar una fase adicional de validación mediante fuzzing.

Finalmente, la herramienta genera un informe consolidado que agrupa toda la información obtenida durante el proceso.

!TODO: insertar diagrama del pipeline completo.

!TODO: insertar referencia a la Figura X.

### 4.2.2. Estructura modular

La implementación de EVMAudit se organiza en varios módulos independientes, cada uno de ellos responsable de una fase concreta del análisis.

Los principales componentes que forman la solución son:

* Runner.
* Normalizer.
* Correlator.
* SWC Catalog.
* Echidna Adapter.
* Reporter.
* Exceptions.

Esta organización permite modificar o ampliar cada componente de forma independiente, favoreciendo la reutilización y evolución futura de la herramienta.

!TODO: insertar diagrama UML de paquetes.

!TODO: revisar nombres definitivos de los módulos.

### 4.2.3. Separación entre lógica de análisis e interfaces

Uno de los principios de diseño adoptados durante el desarrollo fue desacoplar completamente la lógica de análisis de las interfaces de usuario.

Por este motivo, EVMAudit fue implementada como una librería independiente, permitiendo que la funcionalidad principal pueda ser reutilizada desde distintos entornos sin necesidad de modificar el código interno.

Esta decisión permitió desarrollar posteriormente una aplicación web que utiliza la librería como motor de análisis, demostrando la reutilización de la solución propuesta.

Los detalles relacionados con la aplicación web desarrollada y los mecanismos de distribución utilizados se describen en los anexos del documento.

!TODO: referencia cruzada al apartado 4.9.

!TODO: referencia cruzada al Anexo A.

!TODO: referencia cruzada al Anexo B.

!TODO: referencia cruzada al Anexo C.


\newpage


# 4.3.Runner
## 4.3. Módulo Runner

El módulo Runner constituye la capa encargada de la interacción con las herramientas externas utilizadas durante el proceso de análisis. Su principal responsabilidad consiste en gestionar la ejecución de Slither, Mythril y Echidna, así como preparar el entorno necesario para garantizar la correcta realización del análisis.

La existencia de un módulo específico para esta tarea permite desacoplar la lógica propia de EVMAudit de las particularidades de cada herramienta, facilitando la incorporación de nuevas soluciones de análisis en futuras versiones.

!TODO: insertar referencia a la Figura X (diagrama de arquitectura).

### 4.3.1. Responsabilidades del módulo

Las principales responsabilidades implementadas por el módulo Runner son las siguientes:

* detección automática del nombre del contrato
* configuración de la versión del compilador Solidity
* ejecución de Slither
* ejecución de Mythril
* ejecución de Echidna
* almacenamiento de resultados intermedios
* gestión de errores producidos durante la ejecución.

Gracias a esta aproximación, el resto de módulos del sistema pueden trabajar de forma independiente sin necesidad de conocer los detalles específicos de cada herramienta externa.

### 4.3.2. Detección automática del nombre del contrato

Durante las primeras fases de desarrollo se observó que el nombre del fichero Solidity no siempre coincide con el nombre del contrato definido en su interior.

Por este motivo se implementó un mecanismo de detección automática que analiza el código fuente y extrae el nombre real del contrato utilizando expresiones regulares.

Esta decisión permite evitar errores durante las fases posteriores del análisis y elimina la necesidad de que el usuario proporcione manualmente dicha información.

Además, este mecanismo resulta especialmente útil cuando la librería es utilizada desde otras aplicaciones externas, ya que reduce la cantidad de parámetros que deben proporcionarse.

!TODO: insertar fragmento de código de `detect_contract_name()`.

### 4.3.3. Configuración automática del compilador

Las herramientas de análisis empleadas dependen de la versión del compilador Solidity utilizada por el contrato.

Con el objetivo de garantizar la reproducibilidad del análisis y evitar incompatibilidades entre versiones, EVMAudit analiza automáticamente la directiva `pragma solidity` presente en el contrato y configura la versión correspondiente mediante la utilidad `solc-select`.

Este mecanismo permite adaptar dinámicamente el entorno de ejecución y facilita el análisis de contratos desarrollados con diferentes versiones del lenguaje.

!TODO: insertar referencia cruzada a la Sección 2.X (Solidity y compilador).

!TODO: insertar fragmento de código de `_set_solc_version()`.

### 4.3.4. Ejecución de Slither

Slither constituye la primera herramienta utilizada durante el proceso de análisis debido a su rapidez y a la gran cantidad de detectores disponibles.

La función encargada de su ejecución verifica previamente que la herramienta se encuentre instalada y posteriormente lanza el análisis sobre el contrato proporcionado.

Una vez finalizada la ejecución, la salida obtenida se almacena en formato JSON para garantizar la trazabilidad de los resultados.

Durante la implementación fue necesario contemplar ciertos comportamientos específicos de Slither. En particular, la herramienta devuelve el código de salida 255 cuando detecta vulnerabilidades, aunque dicho comportamiento no representa un error real.

Por este motivo, EVMAudit incorpora una lógica específica para interpretar correctamente este caso y continuar con el proceso de análisis.

!TODO: insertar fragmento de código de `run_slither()`.

!TODO: referencia cruzada a la Sección 2.X (Slither).

### 4.3.5. Ejecución de Mythril

La segunda fase del análisis se realiza mediante Mythril, herramienta basada en ejecución simbólica.

A diferencia de Slither, Mythril presenta tiempos de ejecución superiores y requiere parámetros adicionales relacionados con la profundidad máxima de exploración y el tiempo máximo permitido para completar el análisis.

Durante el desarrollo se incorporaron mecanismos para:

* limitar el tiempo máximo de ejecución
* controlar posibles errores durante el análisis
* procesar las salidas generadas por la herramienta
* preservar los resultados originales.

Estas medidas permiten evitar que un contrato especialmente complejo bloquee el proceso completo de análisis.

!TODO: insertar fragmento de código de `run_mythril()`.

!TODO: referencia cruzada a la Sección 2.X (Mythril).

### 4.3.6. Ejecución de Echidna

Una vez generadas las propiedades correspondientes, EVMAudit ejecuta Echidna para realizar una fase adicional de validación mediante fuzzing.

La integración de Echidna presentó una complejidad superior a la observada en Slither y Mythril debido a ciertas particularidades de la herramienta y a las diferencias existentes entre versiones.

Durante el desarrollo fue necesario incorporar mecanismos específicos para:

* reconstruir nombres de propiedades
* interpretar adecuadamente las salidas generadas
* distinguir entre pruebas superadas y vulnerabilidades explotables
* gestionar posibles inconsistencias en los resultados.

Estas adaptaciones permitieron integrar Echidna dentro del flujo general de EVMAudit sin alterar el resto de componentes de la arquitectura.

!TODO: insertar fragmento de código de `run_echidna()`.

!TODO: referencia cruzada a la Sección 2.X (Echidna).

### 4.3.7. Persistencia de resultados intermedios

Con el fin de favorecer la trazabilidad y la reproducibilidad del análisis, EVMAudit almacena las salidas originales generadas por las distintas herramientas utilizadas.

Esta decisión permite:

* inspeccionar manualmente los resultados obtenidos
* reproducir análisis posteriores
* depurar posibles errores
* conservar evidencias originales.

La preservación de las salidas originales resulta especialmente relevante en el contexto de auditorías de seguridad, donde la trazabilidad de los hallazgos constituye un aspecto fundamental.



\newpage


# 4.4.Normalizer
## 4.4. Módulo de normalización

Uno de los principales problemas identificados durante el estudio de las herramientas existentes fue la heterogeneidad de los formatos utilizados para representar las vulnerabilidades detectadas.

Slither y Mythril generan estructuras JSON completamente diferentes, tanto en la forma de representar la severidad como en la descripción de los hallazgos o la identificación de las localizaciones afectadas.

Esta situación dificulta la comparación directa de resultados y hace necesaria una fase previa de transformación antes de poder aplicar mecanismos de correlación.

Para resolver este problema se desarrolló un módulo de normalización encargado de transformar las salidas heterogéneas en una estructura común.

### 4.4.1. Objetivos del proceso de normalización

El proceso de normalización persigue varios objetivos:

* unificar la representación de vulnerabilidades;
* facilitar la correlación entre herramientas;
* preservar las evidencias originales;
* simplificar la generación posterior de informes;
* desacoplar el resto de módulos de las particularidades de cada herramienta.

Gracias a ello, los componentes posteriores pueden operar sobre una estructura homogénea independientemente del origen de los resultados.

### 4.4.2. Estructura común de los hallazgos

Cada vulnerabilidad normalizada se representa mediante un conjunto común de atributos.

Entre los campos principales se encuentran:

* título;
* descripción;
* severidad;
* categoría;
* contrato afectado;
* función afectada;
* localización;
* identificador SWC;
* herramienta de origen;
* evidencia original.

La inclusión de la salida original permite mantener la trazabilidad del análisis y facilita la revisión manual de los resultados.

!TODO: insertar diagrama UML del objeto Finding.

!TODO: revisar nombres exactos de los atributos.

### 4.4.3. Normalización de resultados de Slither

La función de normalización correspondiente a Slither transforma la estructura JSON generada por la herramienta y extrae la información relevante necesaria para construir los hallazgos comunes utilizados por EVMAudit.

Durante esta fase se realiza además la asociación de los detectores propios de Slither con los identificadores SWC correspondientes.

Este proceso permite traducir la terminología específica de Slither a una representación independiente de la herramienta utilizada.

!TODO: insertar fragmento de código de `normalize_slither_output()`.

### 4.4.4. Normalización de resultados de Mythril

De forma análoga, la salida generada por Mythril es procesada para obtener una representación equivalente a la utilizada por Slither.

La transformación permite unificar:

* niveles de severidad;
* nombres de vulnerabilidades;
* identificadores SWC;
* información contextual del hallazgo.

Gracias a ello, ambas herramientas pueden ser tratadas posteriormente de forma transparente por el módulo de correlación.

!TODO: insertar fragmento de código de `normalize_mythril_output()`.

### 4.4.5. Clasificación de vulnerabilidades

Además de unificar la representación de los hallazgos, el módulo de normalización clasifica las vulnerabilidades detectadas siguiendo las categorías definidas durante el estudio del estado del arte.

Entre las categorías utilizadas se encuentran:

* vulnerabilidades de control de acceso;
* vulnerabilidades económicas;
* vulnerabilidades relacionadas con la lógica de negocio;
* vulnerabilidades asociadas a la ejecución del contrato.

Esta clasificación permite mantener la coherencia entre la parte teórica del trabajo y la implementación desarrollada.

!TODO: referencia cruzada a la Sección 2.X (clasificación de vulnerabilidades).

### 4.4.6. Preservación de evidencias

Uno de los principios adoptados durante el diseño de EVMAudit fue evitar la pérdida de información durante las fases intermedias del análisis.

Por este motivo, cada hallazgo normalizado conserva una referencia a la salida original generada por la herramienta correspondiente.

Esta decisión facilita:

* la revisión manual por parte del auditor;
* la trazabilidad del proceso;
* la depuración de errores;
* la reproducibilidad de los resultados.

La conservación de evidencias resulta especialmente importante en entornos de auditoría y análisis forense, donde es necesario justificar el origen de cada vulnerabilidad identificada.

!TODO: insertar diagrama del proceso de normalización.

!TODO: insertar referencia a la Figura X.


\newpage


# 4.5.Correlator
## 4.5. Módulo de correlación

Una vez normalizados los resultados obtenidos por las herramientas de análisis, EVMAudit aplica un proceso de correlación cuyo objetivo consiste en identificar vulnerabilidades equivalentes detectadas por distintas herramientas y agruparlas en un único hallazgo.

Este módulo constituye el núcleo de la contribución desarrollada en el presente Trabajo Fin de Máster, ya que permite reducir la redundancia de información y proporcionar una visión más estructurada de las vulnerabilidades detectadas.

La necesidad de incorporar esta fase surge de una de las principales limitaciones observadas durante el estudio del estado del arte. Aunque herramientas como Slither y Mythril son capaces de detectar un gran número de vulnerabilidades, cada una de ellas presenta los resultados utilizando nomenclaturas y estructuras diferentes, generando además múltiples duplicidades que dificultan la revisión manual por parte del auditor.

Por este motivo, EVMAudit incorpora un mecanismo propio de correlación encargado de consolidar la información procedente de ambas herramientas.

### 4.5.1. Objetivos del proceso de correlación

Los objetivos perseguidos por este módulo son los siguientes:

* reducir la redundancia de información
* agrupar vulnerabilidades equivalentes
* incrementar la confianza en los hallazgos detectados
* facilitar la interpretación de resultados
* proporcionar una representación unificada de las vulnerabilidades.

La correlación no pretende eliminar completamente los falsos positivos generados por las herramientas utilizadas, sino proporcionar una capa adicional de análisis que facilite el trabajo posterior del auditor.

### 4.5.2. Estrategia de correlación

El proceso implementado en EVMAudit se basa en una estrategia de correlación mediante reglas.

Dos vulnerabilidades se consideran equivalentes cuando cumplen simultáneamente las siguientes condiciones:

* afectan al mismo contrato
* afectan a la misma función
* poseen el mismo identificador SWC.

De este modo, la clave utilizada para la correlación puede expresarse de la siguiente forma:

```text
Contrato + Función + SWC
```

Esta aproximación permite agrupar vulnerabilidades que, aunque procedan de herramientas diferentes, representan realmente el mismo problema de seguridad.

La elección del identificador SWC como criterio común permite disponer de una referencia independiente de la nomenclatura utilizada por cada herramienta.

!TODO: insertar referencia cruzada a la Sección 2.X (SWC Registry).

!TODO: insertar pseudocódigo del algoritmo de correlación.

### 4.5.3. Hallazgos confirmados y hallazgos detectados

Una vez realizado el proceso de agrupación, EVMAudit distingue entre dos tipos de vulnerabilidades.

#### Hallazgos confirmados

Se consideran confirmados aquellos hallazgos que han sido detectados por más de una herramienta.

La coincidencia entre distintas técnicas de análisis aumenta la confianza asociada a la vulnerabilidad y proporciona una mayor evidencia de su existencia.

#### Hallazgos detectados

Corresponden a vulnerabilidades identificadas por una única herramienta.

Aunque presentan un menor nivel de confianza, siguen siendo incluidas en el informe final con el objetivo de evitar la pérdida de información potencialmente relevante.

Esta clasificación permite priorizar posteriormente la revisión manual realizada por el auditor.

### 4.5.4. Nivel de confianza

Con el objetivo de proporcionar información adicional sobre la fiabilidad de cada hallazgo, EVMAudit asigna un nivel de confianza basado en las herramientas que han detectado la vulnerabilidad.

La confianza asociada no representa una medida probabilística, sino un indicador orientativo derivado del número de herramientas que coinciden en el mismo hallazgo.

Este mecanismo permite distinguir aquellas vulnerabilidades respaldadas por varias herramientas de aquellas detectadas únicamente por una de ellas.

No obstante, la interpretación final continúa dependiendo del criterio del auditor, ya que la correlación implementada no sustituye la validación manual.

!TODO: revisar nomenclatura definitiva utilizada por el código (`confidence_score`).

### 4.5.5. Gestión de severidades

Cuando una vulnerabilidad es detectada por varias herramientas, puede ocurrir que cada una de ellas asigne niveles de severidad diferentes.

Para resolver esta situación, EVMAudit conserva la severidad más alta reportada por las herramientas implicadas.

Este enfoque se adopta siguiendo un criterio conservador, priorizando la revisión de aquellas vulnerabilidades que potencialmente puedan tener un mayor impacto.

### 4.5.6. Preservación de evidencias

Durante el proceso de correlación se mantiene la información procedente de todas las herramientas que han participado en la detección.

De esta forma, cada hallazgo correlacionado conserva:

* las herramientas que lo han identificado
* las evidencias originales asociadas
* las localizaciones afectadas
* la información contextual proporcionada por cada herramienta.

Esta decisión garantiza la trazabilidad del análisis y facilita la revisión manual posterior.

### 4.5.7. Beneficios del proceso de correlación

La incorporación de esta fase proporciona diversas ventajas:

* reducción de duplicidades
* mejora de la legibilidad del informe final
* aumento de la confianza en determinados hallazgos
* simplificación del proceso de auditoría
* independencia respecto a las herramientas utilizadas.

La correlación constituye, por tanto, uno de los principales elementos diferenciadores de EVMAudit frente al uso individual de las herramientas integradas.

!TODO: insertar diagrama del proceso de correlación.

!TODO: insertar ejemplo real antes y después de la correlación.

!TODO: insertar referencia a la Figura X.




\newpage


# 4.6.SWC Catalog
## 4.6. Catálogo de vulnerabilidades SWC

Con el objetivo de desacoplar la fase de detección de vulnerabilidades de las fases posteriores de validación y generación de pruebas, se implementó un catálogo de vulnerabilidades basado en la clasificación Smart Contract Weakness Classification (SWC).

Este catálogo constituye una capa intermedia que permite asociar los hallazgos detectados con información adicional independiente de las herramientas utilizadas.

Gracias a ello, EVMAudit puede reutilizar la información obtenida durante el proceso de correlación y emplearla posteriormente para la generación automática de propiedades orientadas a Echidna.

### 4.6.1. Objetivos del catálogo

El catálogo desarrollado persigue los siguientes objetivos:

* unificar la representación de vulnerabilidades
* desacoplar la lógica de generación de pruebas
* facilitar la incorporación de nuevas plantillas
* centralizar información sobre las debilidades conocidas
* favorecer la mantenibilidad del sistema.

Esta aproximación permite que las fases posteriores del análisis no dependan directamente de las particularidades de Slither o Mythril.

### 4.6.2. Estructura del catálogo

Cada entrada del catálogo contiene información asociada a una vulnerabilidad concreta.

Entre los datos almacenados se encuentran:

* identificador SWC
* nombre de la vulnerabilidad
* descripción
* severidad
* plantilla asociada
* limitaciones conocidas
* posibilidad de validación automática.

La información almacenada permite enriquecer los hallazgos correlacionados y proporcionar información adicional durante las fases posteriores del análisis.

!TODO: insertar tabla con varios ejemplos del catálogo.

### 4.6.3. Asociación entre detectores y SWC

Una de las principales dificultades observadas durante el desarrollo fue la ausencia de una correspondencia directa entre los detectores utilizados por cada herramienta.

Para resolver este problema se definieron tablas de asociación que permiten traducir los detectores específicos a identificadores SWC.

Gracias a esta estrategia es posible utilizar un lenguaje común durante todo el proceso de análisis y evitar dependencias directas respecto a la nomenclatura propia de cada herramienta.

Esta decisión resulta especialmente relevante para el módulo de correlación descrito anteriormente.

!TODO: insertar referencia cruzada a la Sección 4.4.

### 4.6.4. Reutilización del catálogo

Además de servir como mecanismo de clasificación, el catálogo es utilizado posteriormente durante la generación de propiedades para Echidna.

A partir del identificador SWC asociado a cada vulnerabilidad, EVMAudit recupera automáticamente la plantilla correspondiente y genera las estructuras necesarias para la fase de fuzzing.

Esta aproximación permite separar claramente:

* detección
* correlación
* generación de pruebas.

La independencia entre estas fases facilita futuras ampliaciones y simplifica el mantenimiento del sistema.

### 4.6.5. Extensibilidad del catálogo

La utilización de un catálogo independiente permite incorporar nuevas vulnerabilidades sin necesidad de modificar el resto de módulos implementados.

De esta forma, la incorporación de nuevas entradas únicamente requiere:

1. definir el identificador SWC correspondiente
2. añadir la información descriptiva asociada
3. incorporar la plantilla de generación deseada.

Este diseño favorece la evolución futura de la herramienta y permite adaptar EVMAudit a nuevas versiones del ecosistema Ethereum.

!TODO: insertar diagrama de relación entre SWC Catalog y Echidna Adapter.

!TODO: insertar referencia a la Figura X.


\newpage


# 4.7.Echidna adaptar
## 4.7. Adaptador para Echidna y generación automática de propiedades

Una vez finalizado el proceso de correlación, EVMAudit incorpora una fase adicional orientada a la validación dinámica de determinadas vulnerabilidades mediante fuzzing.

Para ello, se desarrolló un adaptador específico encargado de transformar los hallazgos correlacionados en propiedades compatibles con Echidna, permitiendo complementar los resultados obtenidos mediante análisis estático y ejecución simbólica.

La incorporación de esta fase responde a uno de los objetivos específicos planteados en el trabajo, consistente en combinar distintas técnicas de análisis con el fin de obtener una visión más completa del estado de seguridad del contrato analizado.

!TODO: referencia cruzada a la Sección 3.2 (objetivos específicos).

### 4.7.1. Objetivos del adaptador

El módulo desarrollado persigue los siguientes objetivos:

* reutilizar la información obtenida durante la fase de correlación
* generar automáticamente propiedades para Echidna
* reducir la intervención manual del auditor
* proporcionar una fase adicional de validación
* mantener desacopladas las distintas fases del análisis.

La existencia de este componente permite integrar el fuzzing dentro del pipeline general de EVMAudit sin introducir dependencias directas entre las herramientas utilizadas.

### 4.7.2. Generación de wrappers

Echidna requiere que las propiedades de seguridad estén implementadas como funciones Solidity dentro de un contrato específico.

Con el objetivo de automatizar este proceso, EVMAudit genera dinámicamente un contrato wrapper que hereda del contrato original e incorpora las propiedades correspondientes a las vulnerabilidades detectadas.

El proceso seguido puede resumirse en las siguientes etapas:

1. Recepción de los hallazgos correlacionados.
2. Consulta del catálogo SWC.
3. Obtención de las plantillas asociadas.
4. Sustitución de parámetros.
5. Generación del wrapper final.
6. Ejecución de Echidna.

Gracias a esta aproximación, la generación de pruebas se realiza de forma completamente automática.

!TODO: insertar diagrama del proceso de generación de wrappers.

!TODO: insertar referencia a la Figura X.

### 4.7.3. Plantillas de propiedades

Cada vulnerabilidad soportada dispone de una plantilla específica que describe la propiedad que deberá ser evaluada por Echidna.

Estas plantillas permiten traducir información abstracta procedente del análisis estático a estructuras ejecutables compatibles con el motor de fuzzing.

La utilización de plantillas aporta varias ventajas:

* reutilización de código
* independencia respecto a las herramientas de detección
* facilidad de mantenimiento
* incorporación sencilla de nuevas vulnerabilidades.

!TODO: insertar ejemplo de una plantilla real.

### 4.7.4. Vulnerabilidades testables y no testables

Durante el desarrollo se observó que no todas las vulnerabilidades pueden verificarse automáticamente mediante fuzzing.

Por este motivo, el adaptador distingue entre:

#### Vulnerabilidades testables

Son aquellas que pueden expresarse mediante propiedades directamente evaluables por Echidna.

Algunos ejemplos incluyen:

* determinadas restricciones de acceso
* invariantes económicas
* comprobaciones relacionadas con balances
* validaciones de lógica de negocio.

#### Vulnerabilidades no testables

Corresponden a aquellas situaciones cuya explotación requiere condiciones externas o escenarios complejos difíciles de reproducir automáticamente.

Entre ellas destacan:

* ataques de reentrancia
* determinados problemas de interacción entre contratos
* escenarios dependientes del contexto de despliegue.

En estos casos, EVMAudit conserva la información asociada a la vulnerabilidad y genera advertencias específicas, pero no intenta forzar una validación automática que pudiera producir resultados incorrectos.

Esta decisión se adoptó con el objetivo de evitar conclusiones erróneas y mantener un comportamiento conservador.

### 4.7.5. Integración con Echidna

Una vez generado el wrapper correspondiente, el módulo Runner ejecuta Echidna y recupera los resultados obtenidos durante el proceso de fuzzing.

La salida generada por la herramienta se procesa posteriormente para incorporarla al informe final.

De esta manera, EVMAudit consigue integrar tres técnicas de análisis diferentes:

* análisis estático
* ejecución simbólica
* fuzzing.

La combinación de estas aproximaciones permite aprovechar las fortalezas de cada una de ellas y compensar parcialmente sus limitaciones individuales.

!TODO: referencia cruzada a la Sección 2.X (análisis estático).

!TODO: referencia cruzada a la Sección 2.X (ejecución simbólica).

!TODO: referencia cruzada a la Sección 2.X (fuzzing).

### 4.7.6. Beneficios de la generación automática

La generación automática de propiedades aporta diversas ventajas:

* reducción del trabajo manual
* mayor reutilización de resultados
* integración transparente con Echidna
* facilidad para incorporar nuevas vulnerabilidades
* mejora del flujo general de análisis.

No obstante, la validación automática obtenida no sustituye la revisión manual realizada por el auditor, sino que constituye una capa adicional de apoyo.



\newpage


# 4.8.Gestion de errores
## 4.8. Gestión de errores y robustez de la solución

Debido a la dependencia de herramientas externas y a la complejidad del proceso de análisis, durante el diseño de EVMAudit se prestó especial atención a la gestión de errores y a la robustez del sistema.

La existencia de múltiples componentes externos hace necesario disponer de mecanismos que permitan detectar y manejar situaciones anómalas sin comprometer el funcionamiento global de la herramienta.

### 4.8.1. Necesidad de una gestión centralizada

Durante el proceso de análisis pueden producirse diferentes tipos de errores:

* ausencia de herramientas instaladas
* incompatibilidades entre versiones
* contratos inválidos
* timeouts durante el análisis
* errores internos de las herramientas utilizadas
* problemas durante la generación de wrappers.

La gestión individual de cada una de estas situaciones complicaría considerablemente el mantenimiento del sistema.

Por este motivo se implementó una jerarquía de excepciones propia que centraliza el tratamiento de los errores.

### 4.8.2. Jerarquía de excepciones

La arquitectura implementada incorpora una clase base común a partir de la cual se derivan los distintos tipos de error utilizados por EVMAudit.

Esta aproximación permite distinguir claramente entre:

* errores de configuración
* errores de análisis
* errores producidos por herramientas externas.

La utilización de excepciones específicas simplifica la depuración y mejora la legibilidad del código.

!TODO: insertar diagrama UML de excepciones.

### 4.8.3. Detección de dependencias externas

Antes de ejecutar las herramientas integradas, EVMAudit verifica que las dependencias necesarias se encuentren correctamente instaladas.

Este mecanismo permite detectar problemas de configuración de forma temprana y proporcionar mensajes de error más descriptivos.

La validación previa evita que el proceso de análisis falle de forma inesperada en fases posteriores.

### 4.8.4. Gestión de timeouts

Algunas herramientas, especialmente aquellas basadas en ejecución simbólica, pueden presentar tiempos de análisis elevados dependiendo de la complejidad del contrato.

Con el objetivo de evitar bloqueos indefinidos, EVMAudit incorpora límites temporales para determinadas operaciones.

La utilización de timeouts permite:

* mejorar la estabilidad del sistema
* evitar consumos excesivos de recursos
* garantizar la finalización del análisis.

### 4.8.5. Preservación de resultados ante errores

Cuando se produce un fallo durante alguna fase del análisis, EVMAudit intenta conservar la información obtenida hasta ese momento.

Esta estrategia permite:

* facilitar la depuración
* conservar evidencias parciales
* evitar la pérdida completa del trabajo realizado.

La preservación de resultados resulta especialmente relevante en entornos de auditoría, donde incluso los análisis incompletos pueden aportar información útil.

### 4.8.6. Robustez frente a comportamientos específicos de las herramientas

Durante el desarrollo se detectaron determinados comportamientos particulares en las herramientas integradas.

Entre ellos destacan:

* códigos de retorno no convencionales
* formatos de salida inconsistentes
* diferencias entre versiones
* mensajes mezclados con datos estructurados.

Para hacer frente a estas situaciones se implementaron mecanismos específicos de adaptación y validación.

Estas medidas permitieron integrar las herramientas seleccionadas sin modificar su funcionamiento interno.

### 4.8.7. Beneficios de la estrategia adoptada

La incorporación de mecanismos de gestión de errores proporciona diversas ventajas:

* mayor estabilidad
* mejora de la experiencia de usuario
* facilidad de mantenimiento
* simplificación de la depuración
* incremento de la robustez general del sistema.

La existencia de una capa de gestión de errores independiente contribuye además a mantener desacoplados los distintos módulos que forman la arquitectura de EVMAudit.

!TODO: insertar referencia cruzada al módulo Runner.

!TODO: insertar referencia cruzada al diagrama de arquitectura general.


\newpage


# 4.9.Integración y distribución
## 4.9. Distribución e integración de la solución

Uno de los objetivos perseguidos durante el desarrollo de EVMAudit fue diseñar una solución desacoplada de cualquier interfaz concreta y suficientemente flexible para poder ser reutilizada en distintos contextos.

Por este motivo, la lógica principal de análisis se implementó como una librería independiente, separando completamente las funcionalidades relacionadas con la detección y procesamiento de vulnerabilidades de los mecanismos de interacción con el usuario.

Esta decisión permitió demostrar la reutilización de la solución desarrollada mediante su integración en otros componentes software sin necesidad de modificar el núcleo de la herramienta.

### 4.9.1. Distribución de la librería

La implementación de EVMAudit como una librería independiente permite desacoplar el motor de análisis de cualquier entorno concreto de ejecución.

Este enfoque proporciona diversas ventajas:

* reutilización de la herramienta desde otros proyectos
* separación entre lógica de negocio e interfaces de usuario
* facilidad de mantenimiento
* posibilidad de incorporar nuevas interfaces en el futuro.

La distribución de la librería permite que el proceso de análisis pueda ejecutarse desde aplicaciones externas sin necesidad de duplicar funcionalidades.

!TODO: referencia cruzada al Anexo A (publicación en PyPI).

### 4.9.2. Aplicación web como caso de uso

Con el objetivo de validar la reutilización de la arquitectura desarrollada, se implementó una aplicación web que utiliza EVMAudit como motor de análisis.

La aplicación no implementa mecanismos propios de detección de vulnerabilidades, sino que delega completamente las tareas de análisis en la librería desarrollada.

Esta aproximación permite mantener una única implementación del proceso de análisis y garantiza la consistencia de los resultados obtenidos.

La aplicación actúa, por tanto, como una capa de presentación encargada de:

* recibir contratos inteligentes proporcionados por el usuario
* invocar las funciones de EVMAudit
* mostrar el progreso del análisis
* presentar los resultados obtenidos.

De esta forma, la aplicación web constituye una demostración práctica de la reutilización de la solución desarrollada.

### 4.9.3. Flujo de funcionamiento de la aplicación

La aplicación desarrollada permite dos mecanismos de entrada:

* carga de contratos Solidity mediante fichero
* introducción directa del código fuente a través de la interfaz web.

Una vez recibido el contrato, la aplicación inicia el proceso de análisis y ejecuta internamente el pipeline implementado por EVMAudit.

Las distintas fases del proceso se ejecutan de forma secuencial:

1. ejecución de Slither
2. ejecución de Mythril
3. normalización de resultados
4. correlación de vulnerabilidades
5. generación de propiedades
6. ejecución de Echidna
7. generación del informe final.

Durante la ejecución, la aplicación informa al usuario del progreso alcanzado y permite recuperar el informe una vez finalizado el análisis.

Este comportamiento demuestra que la arquitectura modular adoptada permite integrar EVMAudit en aplicaciones externas sin modificar la lógica interna del sistema.

!TODO: insertar diagrama simplificado de la aplicación web.

!TODO: insertar captura de pantalla de la interfaz.

!TODO: referencia cruzada al Anexo B (aplicación web).

### 4.9.4. Separación entre presentación y lógica de análisis

La decisión de implementar EVMAudit como una librería independiente permite mantener separadas las responsabilidades del sistema.

Mientras que la librería se encarga de:

* ejecutar herramientas externas
* procesar resultados
* correlacionar vulnerabilidades
* generar informes

la aplicación web únicamente proporciona los mecanismos de interacción con el usuario.

Esta separación favorece:

* la mantenibilidad del sistema
* la reutilización de la solución
* la incorporación de nuevas interfaces
* la evolución independiente de cada componente.

En consecuencia, la aplicación web debe entenderse como una demostración de la capacidad de integración de EVMAudit y no como la contribución principal del trabajo.

### 4.9.5. Consideraciones sobre infraestructura

Los aspectos relacionados con la publicación de la librería, el despliegue de la aplicación y la infraestructura utilizada no constituyen el núcleo de la contribución desarrollada en este Trabajo Fin de Máster.

Por este motivo, dichos elementos se incluyen en los anexos del documento.

!TODO: referencia cruzada al Anexo A (PyPI).

!TODO: referencia cruzada al Anexo B (Aplicación web).

!TODO: referencia cruzada al Anexo C (Docker).

!TODO: referencia cruzada al Anexo D (Despliegue).



\newpage


# 4.10. Flujo completo
## 4.10. Flujo completo del análisis

Una vez descritos los distintos módulos que componen EVMAudit, resulta posible analizar el funcionamiento global de la solución.

El proceso completo implementado por la herramienta se compone de varias fases consecutivas que permiten transformar un contrato inteligente en un informe consolidado de vulnerabilidades.

### 4.10.1. Recepción del contrato

El proceso comienza con la recepción del contrato inteligente que se desea analizar.

El contrato puede proceder de distintos orígenes:

* ejecución directa de la librería
* aplicación web desarrollada
* futuras integraciones externas.

Tras recibir el contrato, EVMAudit detecta automáticamente el nombre del contrato y configura la versión adecuada del compilador Solidity.

### 4.10.2. Obtención de resultados mediante Slither y Mythril

La siguiente fase consiste en ejecutar las herramientas de análisis principales.

En primer lugar se ejecuta Slither, aprovechando las ventajas del análisis estático.

Posteriormente se ejecuta Mythril, incorporando las capacidades derivadas de la ejecución simbólica.

La combinación de ambas técnicas permite obtener una cobertura superior a la proporcionada por cada herramienta de forma individual.

!TODO: referencia cruzada a la Sección 2.X (herramientas de análisis).

### 4.10.3. Normalización de resultados

Las salidas generadas por las herramientas se transforman posteriormente a una estructura común.

Este proceso elimina las diferencias existentes entre ambas herramientas y permite trabajar con una representación homogénea de las vulnerabilidades.

La normalización constituye el paso previo necesario para aplicar el mecanismo de correlación.

### 4.10.4. Correlación de vulnerabilidades

Una vez normalizados los resultados, EVMAudit agrupa aquellas vulnerabilidades equivalentes detectadas por varias herramientas.

La correlación permite:

* reducir duplicidades
* aumentar la confianza de determinados hallazgos
* simplificar la interpretación del informe final.

Esta fase representa uno de los principales elementos diferenciadores de la solución desarrollada.

### 4.10.5. Generación de propiedades y fuzzing

A partir de las vulnerabilidades correlacionadas, el sistema consulta el catálogo SWC y genera automáticamente las propiedades necesarias para ejecutar Echidna.

Posteriormente se construye un wrapper Solidity específico y se realiza una fase adicional de validación mediante fuzzing.

Este proceso proporciona información complementaria sobre determinadas vulnerabilidades detectadas durante las fases anteriores.

### 4.10.6. Generación del informe final

Finalmente, toda la información obtenida durante el análisis es consolidada en un informe único.

El informe incluye:

* vulnerabilidades detectadas
* herramientas que las han identificado
* nivel de confianza asociado
* resultados del fuzzing
* metadatos adicionales.

De este modo, el auditor dispone de una visión unificada del estado de seguridad del contrato analizado.

### 4.10.7. Resumen del proceso

El flujo general implementado por EVMAudit puede resumirse en las siguientes etapas:

1. Recepción del contrato.
2. Configuración del entorno.
3. Ejecución de Slither.
4. Ejecución de Mythril.
5. Normalización.
6. Correlación.
7. Consulta del catálogo SWC.
8. Generación del wrapper.
9. Ejecución de Echidna.
10. Generación del informe.

La secuencia completa permite combinar distintas técnicas de análisis dentro de una arquitectura unificada y automatizada.

!TODO: insertar diagrama de secuencia del pipeline completo.

!TODO: insertar diagrama de flujo del proceso.

!TODO: insertar referencia a la Figura X.

!TODO: insertar referencia cruzada a las secciones 4.3 a 4.9.


\newpage


# 4.11.Evaluación experimental
## 4.11. Flujo completo del análisis

Una vez descritos los distintos módulos que componen EVMAudit, resulta posible analizar el funcionamiento global de la solución.

El proceso completo implementado por la herramienta se compone de varias fases consecutivas que permiten transformar un contrato inteligente en un informe consolidado de vulnerabilidades.

### 4.11.1. Recepción del contrato

El proceso comienza con la recepción del contrato inteligente que se desea analizar.

El contrato puede proceder de distintos orígenes:

* ejecución directa de la librería
* aplicación web desarrollada
* futuras integraciones externas.

Tras recibir el contrato, EVMAudit detecta automáticamente el nombre del contrato y configura la versión adecuada del compilador Solidity.

### 4.11.2. Obtención de resultados mediante Slither y Mythril

La siguiente fase consiste en ejecutar las herramientas de análisis principales.

En primer lugar se ejecuta Slither, aprovechando las ventajas del análisis estático.

Posteriormente se ejecuta Mythril, incorporando las capacidades derivadas de la ejecución simbólica.

La combinación de ambas técnicas permite obtener una cobertura superior a la proporcionada por cada herramienta de forma individual.

!TODO: referencia cruzada a la Sección 2.X (herramientas de análisis).

### 4.11.3. Normalización de resultados

Las salidas generadas por las herramientas se transforman posteriormente a una estructura común.

Este proceso elimina las diferencias existentes entre ambas herramientas y permite trabajar con una representación homogénea de las vulnerabilidades.

La normalización constituye el paso previo necesario para aplicar el mecanismo de correlación.

### 4.11.4. Correlación de vulnerabilidades

Una vez normalizados los resultados, EVMAudit agrupa aquellas vulnerabilidades equivalentes detectadas por varias herramientas.

La correlación permite:

* reducir duplicidades
* aumentar la confianza de determinados hallazgos
* simplificar la interpretación del informe final.

Esta fase representa uno de los principales elementos diferenciadores de la solución desarrollada.

### 4.11.5. Generación de propiedades y fuzzing

A partir de las vulnerabilidades correlacionadas, el sistema consulta el catálogo SWC y genera automáticamente las propiedades necesarias para ejecutar Echidna.

Posteriormente se construye un wrapper Solidity específico y se realiza una fase adicional de validación mediante fuzzing.

Este proceso proporciona información complementaria sobre determinadas vulnerabilidades detectadas durante las fases anteriores.

### 4.11.6. Generación del informe final

Finalmente, toda la información obtenida durante el análisis es consolidada en un informe único.

El informe incluye:

* vulnerabilidades detectadas
* herramientas que las han identificado
* nivel de confianza asociado
* resultados del fuzzing
* metadatos adicionales.

De este modo, el auditor dispone de una visión unificada del estado de seguridad del contrato analizado.

### 4.11.7. Resumen del proceso

El flujo general implementado por EVMAudit puede resumirse en las siguientes etapas:

1. Recepción del contrato.
2. Configuración del entorno.
3. Ejecución de Slither.
4. Ejecución de Mythril.
5. Normalización.
6. Correlación.
7. Consulta del catálogo SWC.
8. Generación del wrapper.
9. Ejecución de Echidna.
10. Generación del informe.

La secuencia completa permite combinar distintas técnicas de análisis dentro de una arquitectura unificada y automatizada.

!TODO: insertar diagrama de secuencia del pipeline completo.

!TODO: insertar diagrama de flujo del proceso.

!TODO: insertar referencia a la Figura X.

!TODO: insertar referencia cruzada a las secciones 4.3 a 4.9.


### 4.11.X. Evaluación del contrato con una vulnerabilidad conocida: [NOMBRE DEL CONTRATO]

#### Descripción del contrato

El contrato **[NOMBRE DEL CONTRATO]** fue seleccionado debido a que presenta una vulnerabilidad conocida relacionada con **[TIPO DE VULNERABILIDAD]**.

Este contrato pertenece a **[FUENTE DEL CONTRATO]** y fue incluido en la evaluación con el objetivo de analizar el comportamiento de EVMAudit frente a escenarios representativos.

La vulnerabilidad esperada en este caso corresponde a:

* TODO.

!TODO: referencia cruzada a la Sección 2.X (descripción de la vulnerabilidad).

---

#### Resultados obtenidos por las herramientas

En primer lugar, el contrato fue procesado individualmente por Slither y Mythril.

Los resultados obtenidos se resumen en la Tabla X.

| Herramienta | Vulnerabilidades detectadas |
| ----------- | --------------------------- |
| Slither     | TODO                        |
| Mythril     | TODO                        |

!TODO: insertar referencia a la Tabla X.

---

#### Resultados tras la correlación

Una vez aplicados los mecanismos de normalización y correlación implementados por EVMAudit, se obtuvo un total de **TODO** vulnerabilidades consolidadas.

La Tabla X muestra la relación entre los hallazgos originales y los resultados finales.

| Métrica                      | Valor |
| ---------------------------- | ----- |
| Hallazgos originales         | TODO  |
| Hallazgos correlacionados    | TODO  |
| Vulnerabilidades confirmadas | TODO  |
| Reducción de duplicidades    | TODO  |

!TODO: insertar referencia a la Tabla X.

---

#### Resultados del fuzzing mediante Echidna

A partir de las vulnerabilidades obtenidas se generaron automáticamente las propiedades correspondientes para Echidna.

Los resultados obtenidos fueron los siguientes:

* Propiedades generadas: TODO.
* Propiedades ejecutadas correctamente: TODO.
* Vulnerabilidades verificadas: TODO.
* Limitaciones observadas: TODO.

!TODO: insertar captura o fragmento representativo del resultado de Echidna.

---

#### Discusión

Los resultados obtenidos muestran que **[OBSERVACIÓN PRINCIPAL]**.

En particular:

* TODO.
* TODO.
* TODO.

Este caso pone de manifiesto **[CONCLUSIÓN PRINCIPAL DEL CONTRATO]**.


### 4.11.X. Evaluación del contrato con varias vulnerabilidades: [NOMBRE DEL CONTRATO]

#### Descripción del contrato

El contrato **[NOMBRE]** incorpora una vulnerabilidad relacionada con **[TIPO]**, lo que permite estudiar la capacidad de detección de las herramientas integradas cuando existen varias debilidades simultáneas.

!TODO: describir brevemente el funcionamiento del contrato.

---

#### Comparativa entre herramientas

La Tabla X resume las vulnerabilidades detectadas por cada herramienta.

| Vulnerabilidad | Slither | Mythril |
| :--- | :---: | :---: |
| TODO | [X] | [X] |
| TODO | [X] | [-] |
| TODO | [-] | [X] |
Los resultados muestran que ambas herramientas presentan comportamientos complementarios.

---

#### Efecto del mecanismo de correlación

La aplicación del proceso de correlación permitió:

* eliminar duplicidades;
* unificar nomenclaturas;
* aumentar la confianza de determinados hallazgos.

!TODO: insertar número real de vulnerabilidades correlacionadas.

---

#### Resultados del fuzzing

El proceso de generación automática produjo un total de **TODO** propiedades.

Durante la ejecución de Echidna se observó:

* TODO.

!TODO: describir vulnerabilidades no testables.

---

#### Discusión

Este contrato evidencia que las distintas técnicas de análisis empleadas por EVMAudit permiten obtener información complementaria y mejorar la cobertura respecto al uso individual de cada herramienta.



### 4.11.X. Evaluación del contrato real [NOMBRE DEL CONTRATO]

#### Descripción del contrato

Además de los contratos vulnerables de referencia, se incluyó el contrato **[NOMBRE]**, obtenido de **[REPOSITORIO O FUENTE]**, con el objetivo de analizar el comportamiento de EVMAudit en un escenario más próximo a un entorno real.

!TODO: describir brevemente la finalidad del contrato.

---

#### Resultados obtenidos

La Tabla X resume las vulnerabilidades detectadas durante el análisis.

| Métrica                                 | Valor |
| --------------------------------------- | ----- |
| Vulnerabilidades detectadas por Slither | TODO  |
| Vulnerabilidades detectadas por Mythril | TODO  |
| Vulnerabilidades finales                | TODO  |
| Vulnerabilidades confirmadas            | TODO  |

---

#### Observaciones sobre la correlación

En este caso se observó que:

* TODO.

Asimismo, se identificaron diferencias entre ambas herramientas en relación con:

* TODO.

---

#### Resultados del fuzzing

La fase de fuzzing permitió:

* TODO.

No obstante, algunas vulnerabilidades no pudieron validarse automáticamente debido a:

* TODO.

---

#### Discusión

El análisis realizado demuestra que EVMAudit puede aplicarse también sobre contratos reales y no únicamente sobre ejemplos académicos diseñados específicamente para contener vulnerabilidades.

!TODO: indicar limitaciones observadas durante el análisis.


\newpage




\newpage


# 5. Conclusiones y trabajo futuro

## 5.1 Conclusiones

## 5.2 Limitaciones de la solución
+ **Dependencia de herramientas externas.** EVMAudit depende del correcto funcionamiento de Slither, Mythril y Echidna. Cualquier modificación en dichas herramientas puede afectar al comportamiento del sistema.
+ **Correlación basada en reglas.** La correlación implementada utiliza únicamente:
    + contrato
    + función
    + SWC

    Esto puede provocar que determinadas vulnerabilidades relacionadas no se agrupen correctamente.

+ **Falsos positivos y falsos negativos.** La herramienta no elimina completamente los falsos positivos inherentes a las herramientas integradas.
+ **Limitaciones del fuzzing.** Determinadas vulnerabilidades, como la reentrancia, requieren contratos atacantes específicos y no pueden validarse automáticamente.
+ **Ausencia de análisis inter-contrato.** Actualmente la herramienta analiza cada contrato de forma independiente.
+ **Priorización limitada.** La priorización se basa en la severidad y en el número de herramientas que detectan la vulnerabilidad, sin utilizar métricas más avanzadas como CVSS.

## 5.3 Líneas de trabajo futuro
+ incorporar nuevas herramientas
+ análisis inter-contrato  
+ CVSS
+ Machine Learning
+ Semgrep
+ Manticore
+ dashboard web


\newpage


# Referencias bibliográficas
[1]       S. Nakamoto, “Bitcoin: A Peer-to-Peer Electronic Cash System.” [Online]. Available: www.bitcoin.org

[2]       D. Yaga, P. Mell, N. Roby, and K. Scarfone, “Blockchain Technology Overview,” Jun. 2019, doi: 10.6028/NIST.IR.8202.

[3]       L. Lamport, R. Shostak, and M. Pease, “The Byzantine Generals Problem,” 1982.

[4]       L. Lamport, “Paxos Made Simple,” 2001.

[5]       T. Nakai, A. Sakurai, S. Hironaka, and K. Shudo, “The Blockchain Trilemma Described by a Formula,” in _Proceedings - 2023 IEEE International Conference on Blockchain, Blockchain 2023_, Institute of Electrical and Electronics Engineers Inc., 2023, pp. 41–46. doi: 10.1109/Blockchain60715.2023.00016.

[6]       “¿Qué es el trilema de la blockchain?” Accessed: Apr. 14, 2026. [Online]. Available: https://www.binance.com/es/academy/articles/what-is-the-blockchain-trilemma

[7]       N. Szabo, “Smart Contracts.” Accessed: Apr. 13, 2026. [Online]. Available: https://www.fon.hum.uva.nl/rob/Courses/InformationInSpeech/CDROM/Literature/LOTwinterschool2006/szabo.best.vwh.net/smart.contracts.html

[8]       “Ethereum Smart Contract Best Practices.” Accessed: Apr. 12, 2026. [Online]. Available: https://consensysdiligence.github.io/smart-contract-best-practices/

[9]       DR. GAVIN WOOD, “ETHEREUM: A SECURE DECENTRALISED GENERALISED TRANSACTION LEDGER,” 2025. Accessed: Apr. 12, 2026. [Online]. Available: https://ethereum.github.io/yellowpaper/paper.pdf

[10]     “Chapter 9: Smart Contract Security - Mastering Ethereum.” Accessed: Apr. 15, 2026. [Online]. Available: https://masteringethereum.xyz/chapter_9.html

[11]     “The Architecture of a Web 3.0 application.” Accessed: Apr. 14, 2026. [Online]. Available: https://www.preethikasireddy.com/post/the-architecture-of-a-web-3-0-application

[12]     M. Saad _et al._, “Exploring the Attack Surface of Blockchain: A Systematic Overview”.

[13]     K. Qin, L. Zhou, B. Livshits, and A. Gervais, “Attacking the DeFi Ecosystem with Flash Loans for Fun and Profit,” 2021, pp. 3–32. doi: 10.1007/978-3-662-64322-8_1.

[14]     L. Zhou _et al._, “SoK: Decentralized Finance (DeFi) Attacks,” Apr. 2023, [Online]. Available: http://arxiv.org/abs/2208.13035

[15]     A. Zamyatin _et al._, “SoK: Communication Across Distributed Ledgers.”

[16]     R. Belchior, A. Vasconcelos, S. Guerreiro, and M. Correia, “A Survey on Blockchain Interoperability: Past, Present, and Future Trends,” Nov. 30, 2022, _Association for Computing Machinery_. doi: 10.1145/3471140.

[17]     H. Chu, P. Zhang, H. Dong, Y. Xiao, S. Ji, and W. Li, “A survey on smart contract vulnerabilities: Data sources, detection and repair,” _Inf._ _Softw._ _Technol._, vol. 159, p. 107221, Jul. 2023, doi: 10.1016/j.infsof.2023.107221.

[18]     J. Feist, G. Grieco, and A. Groce, “Slither: A Static Analysis Framework For Smart Contracts,” _Proceedings - 2019 IEEE/ACM 2nd International Workshop on Emerging Trends in Software Engineering for Blockchain, WETSEB 2019_, pp. 8–15, Aug. 2019, doi: 10.1109/WETSEB.2019.00008.

[19]     “crytic/slither: Static Analyzer for Solidity and Vyper.” Accessed: Apr. 14, 2026. [Online]. Available: https://github.com/crytic/slither

[20]     “Smart Contract Security Newsletter #35 | by Shayan Eskandari | Consensys Diligence | Medium.” Accessed: Apr. 14, 2026. [Online]. Available: https://medium.com/consensys-diligence/smart-contract-security-newsletter-35-6411b3d0552b

[21]     S. AL Amri, L. Aniello, and V. Sassone, “A Review of Upgradeable Smart Contract Patterns based on OpenZeppelin Technique,” _The Journal of The British Blockchain Association_, vol. 6, no. 1, pp. 1–8, Apr. 2023, doi: 10.31585/jbba-6-1-(3)2023.

[22]     “Slither - Building Secure Contracts.” Accessed: Apr. 14, 2026. [Online]. Available: https://secure-contracts.com/program-analysis/slither/docs/src/

[23]     “ConsenSysDiligence/mythril: Mythril is a symbolic-execution-based securty analysis tool for EVM bytecode. It detects security vulnerabilities in smart contracts built for Ethereum and other EVM-compatible blockchains.” Accessed: Apr. 14, 2026. [Online]. Available: https://github.com/ConsenSysDiligence/mythril

[24]     B. Mueller, “File 1 of 1 HITB SECCONF Amsterd4m and ConsenSys Dilig3nce bring you Smashing Ethereum Smart Contracts for Fun and Real Profit” 2018.

[25]     “Smart Contract Security Wars: The Ultimate Slither vs Mythril Battle Guide That Saves Your Protocol From Million-Dollar Hacks | by PMartin | CoinsBench.” Accessed: Apr. 14, 2026. [Online]. Available: https://coinsbench.com/%EF%B8%8F-smart-contract-security-wars-the-ultimate-slither-vs-mythril-battle-guide-that-saves-your-837d67c49121

[26]     T. Durieux, J. F. Ferreira, R. Abreu, and P. Cruz, “Empirical Review of Automated Analysis Tools on 47,587 Ethereum Smart Contracts,” _Proceedings - International Conference on Software Engineering_, pp. 530–541, Feb. 2020, doi: 10.1145/3377811.3380364.

[27]     G. Grieco, W. Song, A. Cygan, J. Feist, and A. Groce, “Echidna: Effective, usable, and fast fuzzing for smart contracts,” _ISSTA 2020 - Proceedings of the 29th ACM SIGSOFT International Symposium on Software Testing and Analysis_, pp. 557–560, Jul. 2020, doi: 10.1145/3395363.3404366.

[28]     “crytic/echidna: Ethereum smart contract fuzzer.” Accessed: Apr. 15, 2026. [Online]. Available: https://github.com/crytic/echidna

[29]     “How to use Echidna to test smart contracts | ethereum.org.” Accessed: Apr. 15, 2026. [Online]. Available: https://ethereum.org/developers/tutorials/how-to-use-echidna-to-test-smart-contracts/

[30]     “Security Considerations — Solidity 0.8.35-develop documentation.” Accessed: Apr. 14, 2026. [Online]. Available: https://docs.soliditylang.org/en/latest/security-considerations.html?utm_source=chatgpt.com

[31]     N. Atzei, M. Bartoletti, and T. Cimoli, “A survey of attacks on Ethereum smart contracts (SoK),” Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), vol. 10204 LNCS, pp. 164–186, 2017, doi: 10.1007/978-3-662-54455-6_8/FIGURES/1.

[32]     L. Brent _et al._, “Vandal: A Scalable Security Analysis Framework for Smart Contracts,” Sep. 2018, [Online]. Available: http://arxiv.org/abs/1809.03981

[33]     Jinson Varghese Behanan and Shashank, “OWASP Smart Contract Top 10 | OWASP Foundation.” Accessed: Apr. 12, 2026. [Online]. Available: https://owasp.org/www-project-smart-contract-top-10/

[34]     “EEA EthTrust Security Levels Specification v-after-2 Editor’s Draft.” Accessed: Apr. 12, 2026. [Online]. Available: https://entethalliance.org/specs/ethtrust-sl/#sec-introduction

[35]     C. Ferreira Torres, A. K. Iannillo, A. Gervais, and R. State, “The Eye of Horus: Spotting and Analyzing Attacks on Ethereum Smart Contracts”.

[36]     “Reentrancy Attacks and The DAO Hack Explained | Chainlink.” Accessed: Apr. 15, 2026. [Online]. Available: https://blog.chain.link/reentrancy-attacks-and-the-dao-hack/

[37]     “CoinDesk Turns 10: 2016 - How The DAO Hack Changed Ethereum and Crypto.” Accessed: Apr. 15, 2026. [Online]. Available: https://www.coindesk.com/consensus-magazine/2023/05/09/coindesk-turns-10-how-the-dao-hack-changed-ethereum-and-crypto

[38]     “Ethereum DAO Hack.” Accessed: Apr. 15, 2026. [Online]. Available: https://www.bitstamp.net/learn/crypto-101/ethereum-dao-hack/

[39]     “The Poly Network Hack Explained - Kudelski Security Research Center.” Accessed: Apr. 15, 2026. [Online]. Available: https://kudelskisecurity.com/research/the-poly-network-hack-explained

[40]     R. Zhang, “Analysis and Research on Blockchain Security Technology: A Case Study of the Poly Network Security Incident”, Accessed: Apr. 15, 2026. [Online]. Available: http://www.stemmpress.com

[41]     S. Jiang, W. You, S. Xuan, and J. Shen, “Decentralized finance security: A survey of attacks, defenses, and open challenges,” _High-Confidence Computing_, vol. 6, p. 100383, 2026, doi: 10.1016/j.hcc.2026.100383.

[42]     “bZx Hack Full Disclosure (With Detailed Profit Analysis) | by PeckShield | Medium.” Accessed: Apr. 15, 2026. [Online]. Available: https://peckshield.medium.com/bzx-hack-full-disclosure-with-detailed-profit-analysis-e6b1fa9b18fc

[43]     H. Rezaei, M. Eshghie, K. Anderesson, and F. Palmieri, “SoK: Root Cause of $1 Billion Loss in Smart Contract Real-World Attacks via a Systematic Literature Review of Vulnerabilities,” Sep. 2025, doi: 10.14722/ndss.2025.[23|24]xxxx.

[44]     “Deep Dive Exploit Analysis: Euler Finance.” Accessed: Apr. 15, 2026. [Online]. Available: https://www.cyfrin.io/blog/how-did-the-euler-finance-hack-happen-hack-analysis

[45]     “Euler Finance Flash Loan Attack Explained.” Accessed: Apr. 15, 2026. [Online]. Available: https://www.chainalysis.com/blog/euler-finance-flash-loan-attack/

\newpage


# ANEXO A. Ejemplos de vulnerabilidades en contratos inteligentes

Este anexo presenta ejemplos simplificados de vulnerabilidades representativas en contratos inteligentes desarrollados en Solidity. El objetivo es ilustrar de forma práctica los principales tipos de debilidades descritas en la sección 4.4, facilitando su comprensión y su posterior detección mediante herramientas automáticas.

Cada ejemplo incluye: descripción, fragmento de código vulnerable, impacto y estrategia de mitigación.

## ANEXO A.1. Vulnerabilidades técnicas de ejecución

### ANEXO A.1.1. Reentrancy

La vulnerabilidad de [**reentrancy**](https://www.cyfrin.io/blog/what-is-a-reentrancy-attack-solidity-smart-contracts) se produce cuando un contrato realiza una llamada externa antes de actualizar su estado interno, permitiendo que el contrato receptor reingrese en la función original en un estado inconsistente.

Código vulnerable
```js
contract VulnerableBank {

    mapping(address => uint256) public balances;

    function deposit() public payable {

        balances[msg.sender] += msg.value;

    }

    function withdraw(uint256 amount) public {

        require(balances[msg.sender] >= amount);

        (bool success, ) = msg.sender.call{value: amount}("");

        require(success);

        balances[msg.sender] -= amount;

    }

}
```

- **Impacto**: Un atacante puede drenar fondos repitiendo la llamada antes de que el balance sea actualizado.
- Mitigación:
	- Patrón [_Checks-Effects-Interactions_](https://fravoll.github.io/solidity-patterns/checks_effects_interactions.html)
	- Uso de ReentrancyGuard
	- Actualizar el estado antes de llamadas externas

  
### ANEXO A.1.2. Integer Overflow / Underflow

Errores aritméticos que provocan desbordamientos en operaciones enteras. Aunque mitigados en Solidity >= 0.8, siguen siendo relevantes en bloques unchecked.

Código vulnerable
```js
function increment(uint256 x) public pure returns (uint256) {

    unchecked {

        return x + 1;

    }

}
```

- **Impacto**: Puede alterar balances o condiciones lógicas críticas.
- Mitigación:
	- Evitar unchecked salvo casos justificados
	- Uso de validaciones explícitas

### ANEXO A.1.3. Uso inseguro de delegatecall

La función delegatecall ejecuta código externo en el contexto de almacenamiento del contrato llamador.

Código vulnerable
```js
contract Proxy {

    address public implementation;

    function execute(bytes memory data) public {

        (bool success, ) = implementation.delegatecall(data);

        require(success);

    }

}
```

- **Impacto**: Compromiso total del almacenamiento del contrato.
- Mitigación:
	- Control estricto de la dirección implementation
	- Uso de patrones proxy auditados ([EIP-1967](https://eips.ethereum.org/EIPS/eip-1967), [UUPS](https://docs.openzeppelin.com/contracts-stylus/uups-proxy))

### ANEXO A.1.4. Denegación de servicio (DoS)

Bloqueo de ejecución debido a fallos en llamadas externas o estructuras no acotadas.

Código vulnerable
```js
function payout(address[] memory recipients) public {

    for (uint i = 0; i < recipients.length; i++) {

        payable(recipients[i]).transfer(1 ether);

    }

}
```
- **Impacto**: Un solo fallo revierte toda la operación.
- Mitigación
	- Uso de [patrón _pull over push_](https://medium.com/@markojauregui/the-pull-over-push-model-in-solidity-a-secure-pattern-for-fund-withdrawals-10c2e6628626)
	- Evitar bucles dependientes de input externo

## ANEXO A.2. Vulnerabilidades técnicas de control y privilegios

### ANEXO A.2.1. Falta de control de acceso

Funciones críticas accesibles por cualquier usuario.

Código vulnerable
```js
contract Ownable {

    address public owner;

    function withdrawAll() public {

        payable(msg.sender).transfer(address(this).balance);

    }

}
```

- **Impacto**: Pérdida total de fondos.
- Mitigación:
	- Uso de onlyOwner
	- Librerías como [OpenZeppelin AccessControl](https://docs.openzeppelin.com/contracts/5.x/access-control)

### ANEXO A.2.2. Uso de tx.origin

Uso incorrecto de tx.origin para autenticación.

Código vulnerable
```js
function withdraw() public {

    require(tx.origin == owner);

    payable(msg.sender).transfer(address(this).balance);

}
```
- **Impacto**: Ataques mediante contratos intermediarios.
- **Mitigación**: Usar msg.sender para autenticación

### ANEXO A.2.3. Inicialización insegura (contratos upgradeables)

En contratos upgradeables, la inicialización se realiza mediante funciones externas (initialize) en lugar de constructores. Si no están protegidas, cualquier usuario puede ejecutarlas y asumir el control del contrato.

Código vulnerable
```js
function initialize(address _owner) public {

    owner = _owner;

}
```
- **Impacto**: Un atacante puede inicializar el contrato antes que el legítimo propietario.
- Mitigación:
	- Uso de [initializer (OpenZeppelin)](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable)
	- Bloqueo de inicialización tras ejecución

## ANEXO A.3. Vulnerabilidades económicas y del entorno

### ANEXO A.3.1. Front-running / MEV

Un atacante observa la mempool y ejecuta transacciones antes que la víctimANEXO A.

Código vulnerable
```js
function buy(uint price) public {

    require(price == currentPrice);

    // compra

}
```
- **Impacto**: Manipulación de operaciones (arbitraje, liquidaciones, subastas).
- Mitigación:
	- [_Commit-reveal_](https://medium.com/coinmonks/commit-reveal-scheme-in-solidity-c06eba4091bb)
	- Subastas ciegas
	- Uso de _relayers_ privados

### ANEXO A.3.2. Dependencia de oráculos

Uso de datos externos manipulables.

Código vulnerable
```js
function getPrice() public view returns (uint) {

    return externalOracle.price();

}
```

- **Impacto**: Manipulación de precios en DeFi.
- Mitigación:
	- Oráculos descentralizados (ej. [Chainlink](https://chain.link/))
	- Promedios temporales ([TWAP](https://www.binance.com/es-MX/support/faq/detail/80655cc54d8a4b2bb8ea097001844fd1))

### ANEXO A.3.3. Uso de block.timestamp

El uso de block.timestamp como fuente de aleatoriedad o para decisiones críticas es inseguro, ya que su valor puede ser parcialmente manipulado por mineros o validadores dentro de ciertos límites.

Código vulnerable
```js
function random() public view returns (uint) {

    return uint(keccak256(abi.encodePacked(block.timestamp)));

}
```
- **Impacto**: Resultados predecibles o manipulables por mineros/validadores.
- Mitigación:
	- VRF ([Verifiable Random Functions](https://chain.link/education-hub/verifiable-random-function-vrf))
	- Fuentes externas verificables

## ANEXO A.4. Errores lógicos de negocio

### ANEXO A.4.1. Error en cálculo de balances

Errores en operadores lógicos o condiciones de validación pueden provocar inconsistencias en la gestión de balances, especialmente en casos límite donde las condiciones no cubren todos los escenarios posibles.

Código vulnerable
```js
function withdraw(uint amount) public {

    require(balances[msg.sender] > amount);

    balances[msg.sender] -= amount;

}
```
- **Impacto**: Comportamiento incorrecto en condiciones límite.
- Mitigación:
	- Uso de > en lugar de >=.

### ANEXO A.4.2. Distribución incorrecta de recompensas

La lógica de distribución puede introducir errores debido a divisiones enteras o falta de gestión de restos, provocando pérdida de precisión y fondos no asignados correctamente.

Código vulnerable
```js
function distribute() public {

    uint reward = total / users.length;

    for (uint i = 0; i < users.length; i++) {

        balances[users[i]] += reward;

    }

}
```
- Impacto:
	- Pérdida de fondos debido a errores de redondeo (truncamiento en división entera)
	- Acumulación de saldo no distribuido en el contrato
	- Distribuciones injustas entre usuarios
	- Posibles vectores de explotación si un atacante manipula el número de participantes

- Mitigación:
	- Uso de patrones de distribución que gestionen residuos (por ejemplo, acumuladores o “_remainder handling_”)
	- Empleo de mayor precisión mediante escalado ([_fixed-point arithmetic_](https://rareskills.io/post/solidity-fixed-point))
	- Validación de invariantes económicas (la suma distribuida debe coincidir con el total)
	- Testing específico de casos límite (número de usuarios, valores pequeños, etc.)

### ANEXO A.4.3. Estados inconsistentes

La falta de control adecuado sobre las transiciones de estado puede permitir la ejecución de funciones en condiciones no válidas, generando comportamientos inconsistentes en el contrato.

Código vulnerable
```js
enum State { Open, Closed }

State public state;

function close() public {

    state = State.Closed;

}

function bid() public payable {

    require(state == State.Open);

}
```
- Impacto:
	- Ejecución de funciones en estados no válidos
	- Comportamiento inesperado del contrato
	- Bloqueo o bypass de lógica de negocio
	- Posible explotación combinada con otras vulnerabilidades (por ejemplo, _front-running_ o _reentrancy_
- Mitigación:
	- Implementación de máquinas de estados explícitas y completas
	- Uso de modificadores para validar estado (inState(State.Open))
	- Restricción de transiciones de estado válidas
	- Aplicación de patrones [_state machines_](https://fravoll.github.io/solidity-patterns/state_machine.html)

## ANEXO A.5. Resumen de vulnerabilidades

| **_ID_** | **Categoría** | **Vulnerabilidad**    | **Tipo**            | **Impacto** | **Detectable automáticamente** | **Ejemplo sección** |
| -------- | ------------- | --------------------- | ------------------- | ----------- | ------------------------------ | ------------------- |
| _V1_     | Técnica       | Reentrancy            | Ejecución           | Crítico     | Sí (Slither/Mythril)           | ANEXO A.1.1               |
| _V2_     | Técnica       | Overflow              | Aritmético          | Medio       | Sí (Slither)                   | ANEXO A.1.2               |
| _V3_     | Técnica       | Delegatecall          | Ejecución           | Crítico     | Parcial                        | ANEXO A.1.3               |
| _V4_     | Control       | Acceso no restringido | Autorización        | Crítico     | Sí                             | ANEXO A.2.1               |
| _V5_     | Control       | tx.origin             | Autenticación       | Alto        | Sí                             | ANEXO A.2.2               |
| _V6_     | Económica     | Front-running         | MEV                 | Alto        | No                             | ANEXO A.3.1               |
| _V7_     | Económica     | Oráculos              | Dependencia externa | Crítico     | No                             | ANEXO A.3.2               |
| _V8_     | Lógica        | Error de balance      | Lógica              | Variable    | No                             | ANEXO A.4.1               |

\newpage


# ANEXO B. Entorno virtual Python

El desarrollo de una librería Python destinada a integrar múltiples herramientas de análisis de seguridad plantea, desde el inicio, un problema de gestión de dependencias que no debe subestimarse. Las herramientas que se integran en la solución propuesta, como Slither, Mythril o Echidna, tienen requisitos de versión específicos y en ocasiones incompatibles entre sí cuando se instalan en el entorno global del sistema. Esta situación, conocida en el ecosistema Python como dependency hell, puede provocar conflictos silenciosos difíciles de depurar y comprometer la reproducibilidad del entorno de desarrollo.

Un entorno virtual (virtual environment) es un directorio aislado que contiene una instalación independiente del intérprete Python junto con sus propios paquetes y dependencias, sin interferir con el sistema global ni con otros proyectos. Esta separación proporciona varias ventajas fundamentales en el contexto del presente trabajo:

En primer lugar, garantiza el **aislamiento de dependencias**, de forma que cada proyecto mantiene sus propias versiones de bibliotecas sin afectar al resto del sistema. Esto resulta especialmente relevante cuando diferentes herramientas de análisis requieren versiones distintas de una misma dependencia transitiva.

En segundo lugar, favorece la **reproducibilidad del entorno de desarrollo**. Todos los integrantes del equipo pueden trabajar exactamente con las mismas versiones de todas las dependencias, eliminando la variabilidad asociada a instalaciones manuales y garantizando que los resultados obtenidos durante el desarrollo son consistentes independientemente del sistema operativo o configuración personal de cada desarrollador.

En tercer lugar, facilita el **ciclo de vida** del proyecto al delimitar claramente qué paquetes pertenecen al proyecto y cuáles son del sistema, simplificando tanto la distribución de la librería como su posterior publicación en registros públicos como PyPI.

## ANEXO B.1. Tipos de entornos virtuales

En el ecosistema Python existen varias alternativas para la gestión de entornos virtuales, con distintos niveles de abstracción y funcionalidad.

El módulo estándar `venv`, incluido en la biblioteca estándar desde Python 3.3, permite crear entornos virtuales básicos mediante el comando `python -m venv .venv`. Sin embargo, este enfoque no incluye gestión de dependencias ni ficheros de bloqueo (*lockfiles*), por lo que debe complementarse con herramientas adicionales como `pip` y `pip-tools`.

`virtualenv` es una alternativa anterior al módulo estándar, con mayor compatibilidad con versiones antiguas de Python y algunas funcionalidades adicionales, aunque en la práctica ha quedado desplazada por las herramientas modernas.

`conda` ofrece un modelo más completo que combina gestión de entornos con gestión de paquetes, incluyendo dependencias no Python. Es habitual en entornos científicos y de análisis de datos, pero introduce una complejidad y un tamaño innecesarios para un proyecto centrado en el ecosistema Python puro.

Herramientas como `poetry` o `pipenv` representan un nivel superior de abstracción, combinando la gestión de entornos virtuales con la resolución de dependencias, la generación de ficheros de bloqueo y el ciclo de publicación de paquetes. Su adopción en proyectos profesionales se ha generalizado en los últimos años.

Finalmente, `uv` constituye la herramienta de última generación en este espacio, combinando todas las funcionalidades anteriores en una solución de rendimiento muy superior, como se detalla en la sección siguiente.

## ANEXO B.2. Herramienta a usar: uv

`uv` es un gestor de paquetes y proyectos Python de alto rendimiento desarrollado por Astral, la empresa creadora del formateador Ruff. Implementado en Rust, se presenta como una herramienta unificada capaz de sustituir a `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine` y `virtualenv` mediante una interfaz de línea de comandos coherente. Su desarrollo se orienta tanto a la velocidad de ejecución como a la corrección en la resolución de dependencias y a la facilidad de adopción en proyectos de diferente escala y complejidad.

### ANEXO B.2.1. Ventajas de uv

La principal ventaja diferencial de `uv` respecto a las alternativas existentes es su rendimiento. Según los propios *benchmarks* publicados en su documentación oficial, `uv` es entre 10 y 100 veces más rápido que `pip` en operaciones de instalación de paquetes con caché caliente. Esta diferencia resulta perceptible en la práctica, especialmente durante las fases de incorporación de nuevos integrantes al equipo o en entornos de integración continua donde el entorno debe reconstruirse frecuentemente.

Más allá del rendimiento, `uv` ofrece un conjunto de ventajas relevantes para el desarrollo de la librería propuesta en este trabajo. Gestiona automáticamente los entornos virtuales asociados a cada proyecto, sin necesidad de crearlos ni activarlos manualmente. Genera y mantiene un fichero de bloqueo universal (`uv.lock`) que garantiza instalaciones reproducibles en cualquier plataforma. Permite gestionar múltiples versiones del intérprete Python e instalar la versión adecuada de forma automática si no está disponible en el sistema. Además, su diseño es compatible con los estándares del ecosistema Python (`pyproject.toml`, PEP 517, PEP 621), lo que facilita la integración con otras herramientas y la publicación en registros de paquetes.

### ANEXO B.2.2. Qué proporciona uv en el contexto de este proyecto

Para el desarrollo de la librería propuesta, uv proporciona un conjunto de funcionalidades que cubren todo el ciclo de vida del proyecto, desde la inicialización hasta la publicación.

**Gestión de dependencias y sincronización del entorno.** Una vez definidas las dependencias del proyecto en el fichero `pyproject.toml`, cualquier integrante del equipo puede reproducir exactamente el mismo entorno ejecutando un único comando:
```bash
uv sync
```

Este comando resuelve las dependencias declaradas, instala las versiones exactas registradas en el fichero de bloqueo `uv.lock` y configura el entorno virtual del proyecto de forma automática. La simplicidad de este flujo elimina los problemas habituales de divergencia entre entornos de desarrollo individuales, garantizando que todos los miembros del equipo trabajan con las mismas versiones de Slither, Mythril, Echidna y el resto de dependencias de la librería.

**Inicialización de proyectos.** `uv` proporciona soporte integrado para la creación de nuevos proyectos mediante el comando `uv init`. Para el caso específico de una librería Python destinada a ser importada por otros proyectos o publicada en PyPI, se utiliza la opción `--lib`:
```bash
uv init --lib evmaudit
```

Este comando genera automáticamente la estructura de directorios recomendada para una librería Python, incluyendo el fichero `pyproject.toml` con los metadatos del proyecto, el directorio `src/` con el paquete principal y los ficheros de configuración necesarios para la construcción y distribución. El uso de la disposición `src/` (*src layout*) es la práctica recomendada actualmente para proyectos publicables, ya que evita problemas habituales relacionados con la importación del paquete desde el directorio raíz durante el desarrollo.

**Construcción de distribuciones.** `uv` integra soporte nativo para la generación de distribuciones instalables mediante el comando `uv build`, que produce tanto el archivo fuente (*sdist*) como la rueda binaria (*wheel*) del paquete:

```bash
uv build
```

El resultado son los artefactos estándar de distribución Python ubicados en el directorio `dist/`, listos para ser publicados o distribuidos directamente.

**Publicación de paquetes.** El ciclo se completa con el soporte para publicación en registros de paquetes, incluyendo PyPI, mediante el comando `uv publish`:
```bash
uv publish
```

Este comando gestiona la autenticación y la subida de los artefactos generados, cubriendo el flujo completo que anteriormente requería herramientas adicionales como `twine`.

En conjunto, `uv` unifica en una sola herramienta todo el ciclo de vida del proyecto: inicialización, gestión de dependencias, sincronización del entorno, construcción de distribuciones y publicación. Esta integración reduce la fricción en el desarrollo colaborativo y facilita la adopción de prácticas profesionales de gestión de proyectos Python desde las primeras fases del trabajo.


\newpage


# ANEXO C.	DISTRIBUCIÓN Y PUBLICACIÓN EN EL REGISTRO DE PAQUETES PYPI

El ciclo de desarrollo de la librería propuesta culmina con su fase de distribución, permitiendo que las herramientas de análisis de seguridad implementadas sean accesibles e integrables por la comunidad de desarrollo y auditoría de *smart contracts*. Para asegurar una distribución estandarizada y eficiente dentro del ecosistema Python, se ha seleccionado el índice oficial de paquetes PyPI (*Python Package Index*). La gestión de este proceso se unifica bajo la herramienta `uv`, garantizando la consistencia desde la compilación de los artefactos hasta su publicación definitiva.
## ANEXO C.1. Configuración de Metadatos del Proyecto (pyproject.toml)

El paso previo indispensable para la distribución consiste en la definición inequívoca de los metadatos y la especificación del sistema de construcción (*build system*) en el archivo de configuración `pyproject.toml`, ubicado en la raíz del paquete. Este procedimiento se rige bajo los estándares modernos de empaquetado de Python (PEP 517 y PEP 621).

Para este proyecto, se ha adoptado `hatchling` como *build backend*, debido a su ligereza, velocidad y compatibilidad nativa con las especificaciones del ecosistema actual. A continuación, se presenta la estructura de configuración requerida para delimitar las propiedades de la librería `evmaudit`:

```toml
[project]
name = "evmaudit"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
authors = [
    { name = "Daniel Rovira Martínez", email = "pardalaco@gmail.com" },
    { name = "Paula Suárez Prieto", email = "Paula Suárez Prieto" },
    { name = "Adrián Moreno Martín", email = "adrimore2@gmail.com" }
]
requires-python = ">=3.12"
dependencies = [
    "eth>=0.0.1",
    "mythril>=0.24.8",
    "setuptools<70.0.0",
    "slither-analyzer>=0.9.2",
    "solc-select>=1.2.0",]

[project.scripts]
evmaudit = "evmaudit.main:main"

[build-system]
requires = ["uv_build>=0.11.15,<0.12.0"]
build-backend = "uv_build"
```

Los clasificadores (*classifiers*) incluidos permiten categorizar la librería dentro del índice público, facilitando su indexación en función de la licencia de código abierto seleccionada, la compatibilidad del sistema operativo y las versiones soportadas del intérprete Python.

## ANEXO C.2. Proceso de Compilación del Paquete
Una vez validados los metadatos, se procede a la generación de los archivos de distribución. Este proceso transforma el código fuente estructurado en el directorio `src/` en artefactos instalables e independientes del entorno de desarrollo.

La ejecución del comando unificado de compilación abstrae la complejidad de las herramientas tradicionales:

```bash
uv build
```

Este comando genera de forma nativa dos tipos de distribuciones estándar dentro del directorio `dist/`:

- **Distribución de código fuente (*sdist* o** `.tar.gz`**):** Un archivo comprimido que contiene el código fuente original y los archivos de configuración, actuando como respaldo para plataformas o configuraciones no previstas.
- **Distribución binaria compilada (*wheel* o** `.whl`**):** El formato de empaquetado moderno que permite una instalación directa y optimizada en el sistema destino, evitando la necesidad de compilar el código en la máquina del usuario final.

En contextos de desarrollo complejos donde el paquete forma parte de un repositorio principal o arquitectura de *workspace* (como el entorno de trabajo `TFM-UNIR`), `uv` permite gestionar la compilación de manera localizada. Para forzar la construcción exclusiva del subproyecto desde su propio directorio y evitar colisiones en la raíz global, se aplica la opción de empaquetado específico:

```bash
    uv build --package evmaudit
```

## ANEXO C.3. Seguridad y Autenticación en la Publicación

La publicación de código en repositorios públicos exige mecanismos estrictos de control de acceso para prevenir vectores de ataque basados en la cadena de suministro (*supply chain attacks*). Por razones de seguridad, se desestima el uso de contraseñas de usuario tradicionales en favor de la autenticación basada en **Tokens de API.**

El proceso de despliegue requiere la obtención de un *token* con prefijo `pypi-` generado desde el panel de control de PyPI. En la primera interacción, el alcance del *token* se configura de manera global; no obstante, una vez realizada la primera subida con éxito, la buena práctica metodológica dicta restringir los permisos del token de manera exclusiva al ámbito del paquete `evmaudit`, minimizando así la superficie de exposición en caso de compromiso de la credencial.

## ANEXO C.4. Ejecución del Despliegue

Con los artefactos ubicados en el directorio `dist/` y las credenciales expedidas, se procede a la transferencia segura hacia los servidores de PyPI. El comando `uv publish` automatiza la verificación de integridad mediante *hashes* criptográficos y realiza la subida en un único paso:

```bash
uv publish
```

Durante el flujo interactivo en la línea de comandos, el sistema requiere la introducción del identificador genérico `__token__` en el campo de usuario, seguido de la clave alfanumérica del token de API en el campo de contraseña. Con el objetivo de optimizar este flujo en entornos de Integración Continua (CI/CD) o evitar la inserción manual recurrente, es posible exportar temporalmente la credencial en el entorno de la terminal actual:


```bash
export UV_PUBLISH_TOKEN="pypi-tu-token-aqui"
uv publish
```

Tras la finalización exitosa del proceso, el paquete queda registrado globalmente, permitiendo su incorporación inmediata en otros proyectos mediante los gestores tradicionales del ecosistema:
```bash
pip install evmaudit
```

O bien, aprovechando los beneficios de rendimiento de la herramienta unificada del proyecto:
```bash
uv add evmaudit
```

## ANEXO C.5. Ciclo de Mantenimiento y Actualización de Versiones

La evolución de la librería para la corrección de vulnerabilidades o la integración de nuevas capacidades de análisis requiere una política estricta de control de versiones. El flujo metodológico establecido para la liberación de actualizaciones iterativas consta de tres fases secuenciales:
- **Incremento del número de versión:** Modificación manual del campo `version` en el archivo `pyproject.toml` siguiendo el estándar de Versionado Semántico (ej. de `0.1.0` a `0.1.1`).
- **Saneamiento del directorio de distribución:** Eliminación de los artefactos obsoletos del directorio `dist/` para mitigar el riesgo de duplicidad o subidas erróneas de versiones previas.
- **Reconstrucción y despliegue:** Ejecución consecutiva de los procesos de empaquetado y transferencia:

```bash
uv build
uv publish
```

Esta sistemática asegura que cada iteración de la herramienta de auditoría de la EVM mantenga la trazabilidad, la coherencia histórica y la disponibilidad pública necesarias para un entorno de producción académica y profesional.

 


\newpage




\newpage


# Anexo D Docker

## ANEXO D.1.	CONTENEDORIZACIÓN E INFRAESTRUCTURA DE DESPLIEGUE (DOCKER)

En el ámbito del desarrollo de software moderno y la ciberseguridad, la reproducibilidad del entorno de ejecución constituye un pilar crítico. Tradicionalmente, el despliegue de aplicaciones que integran múltiples herramientas de análisis (como compiladores de Solidity y motores de ejecución simbólica) se enfrentaba al problema de "funciona en mi máquina", derivado de las discrepancias en las versiones de las dependencias, librerías del sistema operativo y configuraciones locales. Para mitigar este riesgo, el presente proyecto adopta una arquitectura basada en contenedores de aplicación a través del ecosistema de **Docker** y **Docker Compose**.

## ANEXO D.2.	Fundamentos de Contenedorización: Docker y Docker Compose

Docker es una plataforma de código abierto basada en la tecnología de contenedorización, la cual permite empaquetar una aplicación y todas sus dependencias (binarios, librerías, archivos de configuración) en una unidad estandarizada denominada **contenedor**. A diferencia de la virtualización tradicional, Docker opera mediante la virtualización a nivel de sistema operativo, compartiendo el núcleo (kernel) del sistema anfitrión pero ejecutando los procesos en espacios de usuario completamente aislados a través de namespaces y cgroups. Desde la perspectiva de la seguridad, este aislamiento garantiza que los procesos del pipeline de auditoría de EVMAudit se ejecuten de forma confinada, mitigando el impacto en la infraestructura anfitriona ante la eventual ejecución de código arbitrario o inesperado durante el análisis de contratos inteligentes.

Por su parte, **Docker Compose** es la herramienta diseñada para definir y orquestar aplicaciones Docker multi-contenedor. Mediante el uso de un archivo de configuración declarativo en formato YAML (docker-compose.yml), permite definir con precisión los servicios que componen el sistema, sus dependencias de arranque, la exposición de puertos hacia el exterior, la creación de redes aisladas y la asignación de volúmenes persistentes. En el contexto de EVMAudit, actúa como el motor de despliegue unificado, permitiendo al administrador inicializar toda la infraestructura del TFM (servidor FastAPI, interfaz web y almacenamiento de informes) de manera centralizada.

## ANEXO D.3.	Estrategia de Construcción de la Imagen (Dockerfile)
La construcción de la imagen se define en un único Dockerfile optimizado. Debido a que el pipeline de análisis requiere interactuar con el sistema operativo para invocar compiladores y binarios de seguridad, se ha seleccionado **Ubuntu 22.04** como imagen base, proporcionando un entorno estable y con soporte extendido para dependencias nativas de Linux en arquitectura amd64.

El proceso de aprovisionamiento de la imagen se divide en las siguientes fases críticas:
1. **Entorno y Variables de Sistema**: Se configuran las variables de entorno `PYTHONDONTWRITEBYTECODE=1` y `PYTHONUNBUFFERED=1` para optimizar la ejecución de Python dentro del contenedor, evitando la escritura de residuos binarios y forzando el volcado de logs en tiempo real. Asimismo, se establece `DEBIAN_FRONTEND=noninteractive` para suprimir diálogos interactivos durante la instalación de paquetes.
2. **Aprovisionamiento de Compiladores (Solidity):** Se añade el repositorio PPA oficial de Ethereum (ppa:ethereum/ethereum) para incorporar el compilador nativo de Solidity (solc). Posteriormente, se instala la utilidad `solc-select` mediante el gestor de paquetes de Python para automatizar la descarga y conmutación de versiones.
3. **Integración del Fuzzer Echidna:** Dado que Echidna se distribuye de manera óptima como un binario estático para Linux, el contenedor automatiza su descarga directa (versión v2.3.2) desde los repositorios oficiales de *Crytic*, procediendo a su extracción e instalación en `/usr/local/bin/` para garantizar su disponibilidad inmediata en el PATH del sistema.
4. **Optimización de Dependencias con `uv` (Multi-stage Build):** Con el objetivo de minimizar los tiempos de construcción y asegurar una gestión eficiente de los paquetes de Python, se emplea un mecanismo de construcción en etapas múltiples (Multi-stage build), importando los binarios optimizados del gestor uv directamente desde su imagen oficial en el registro de GitHub (ghcr.io/astral-sh/uv:latest).
5. **Instalación del Paquete Local:** Tras establecer el directorio de trabajo en /app y copiar el código fuente , se ejecuta el comando `uv sync --frozen --no-cache`. Esto resuelve de forma determinista el grafo de dependencias del archivo uv.lock, registrando el paquete local editable evmaudit e instalando el servidor ASGI Uvicorn sin almacenar datos residuales en la caché de la imagen.

## ANEXO D.4.	Orquestación de Servicios (Docker Compose)

La coordinación del contenedor web y sus dependencias con el sistema anfitrión se gestiona de forma declarativa mediante un archivo docker-compose.yml. La especificación del servicio, denominado evmaudit-web, se fundamenta en tres pilares de ingeniería:

- **Persistencia de Datos mediante Volúmenes**: Con el fin de dotar al sistema de un estado persistente (pese a la naturaleza efímera de los contenedores), se realiza un mapeo directo de directorios del host hacia el contenedor:
- **`./jsons/_uploads:/app/jsons/_uploads`**: Almacena de forma persistente los contratos Solidity cargados por los usuarios, los wrappers intermedios generados para Echidna y los informes de auditoría finales en formato JSON y Markdown.
- **`./contracts:/app/contracts`**: Habilita un volumen opcional para la auditoría directa de Smart Contracts locales sin necesidad de interactuar con la interfaz web.
- **Aislamiento de Red y Mapeo de Puertos**: Se expone el puerto 8080 del contenedor hacia el puerto 8080 del sistema anfitrión. Esto permite redirigir el tráfico HTTP de la interfaz construida en HTML5/Vanilla JS hacia el backend desarrollado en FastAPI de forma transparente.
- **Tolerancia a Fallos**: Se implementa la política de reinicio restart: unless-stopped. Esta directiva asegura la alta disponibilidad del servicio ante excepciones imprevistas en el motor de ejecución simbólica (Mythril) o caídas del propio demonio de Docker, garantizando que el servicio web vuelva a levantarse de manera automática salvo interrupción explícita del administrador.

## ANEXO D.5.	Flujo de Despliegue y Ciclo de Vida del Contenedor
Para la puesta en marcha de la infraestructura local en entornos de desarrollo o evaluación, el ciclo de vida del contenedor se administra mediante el estándar de comandos de Docker Compose:
1. **Fase de Construcción (Build):** Compilación de la imagen e instalación del entorno virtual determinista:
```bash
docker compose build
```

2. **Fase de Inicialización (Up):** Despliegue e instanciación del servicio en segundo plano (detached mode):
```bash
docker compose up -d
```

3.	**Fase de Auditoría de Ejecución (Logs):** Inspección de la salida estándar del contenedor para la monitorización de los análisis en curso:

```bash
docker compose logs -f evmaudit-web
```

4.	**Fase de Parada (Down):** Interrupción y eliminación de los contenedores activos salvaguardando la integridad de los datos de las auditorías gracias a los volúmenes enlazados:
docker compose down



\newpage


# ANEXO F.	ENTORNO DE INTEGRACIÓN CONTINUA (CI/CD) Y PUBLICACIÓN AUTOMATIZADA

Para garantizar la integridad del software durante el ciclo de vida del desarrollo y agilizar el flujo de despliegue, se ha diseñado e implementado un pipeline de Integración Continua (CI) basado en **GitHub Actions**. Esta estrategia de ingeniería de software permite automatizar la compilación, verificación y empaquetado de la aplicación en cada iteración, mitigando los riesgos asociados a la integración manual de código y asegurando la disponibilidad inmediata de artefactos listos para producción.

## ANEXO F.1.	Arquitectura del Workflow y Disparadores (Triggers)

El flujo de trabajo automatizado se define de manera declarativa mediante la sintaxis YAML de GitHub Actions. Con el propósito de optimizar los recursos de cómputo y mantener un control estricto sobre la estabilidad de la rama principal, se han configurado dos disparadores específicos:

- **Eventos de Empuje (*Push*):** El pipeline se ejecuta de forma automática ante cualquier consolidación directa de código en la rama `main`, asegurando que cada incremento de software sea evaluado y empaquetado de inmediato.

- **Solicitudes de Extracción (*Pull Requests*):** La automatización actúa como una barrera de calidad (*quality gate*) ante cualquier intento de fusión hacia la rama `main`. Esto permite validar que las modificaciones propuestas por los desarrolladores no rompan el proceso de construcción del contenedor antes de que el código sea integrado definitivamente.

El entorno de ejecución seleccionado para los trabajos (*jobs*) es `ubuntu-latest`, lo que proporciona un entorno virtual limpio, aislado y actualizado de manera nativa por la infraestructura de GitHub.

## ANEXO F.2.	Desglose Técnico de las Etapas del Pipeline
El ciclo de vida del pipeline se divide en dos trabajos secuenciales y dependientes, los cuales ejecutan tareas críticas de aprovisionamiento, autenticación y despliegue:
 

### ANEXO F.2.1.	Trabajo de Construcción y Publicación (`create-docker-image`)

Es el núcleo técnico de la automatización y consta de los siguientes pasos detallados:

1.  **Clonación del Repositorio y Gestión de Submódulos:** Se utiliza la acción oficial `actions/checkout@v2`. Debido a la arquitectura desacoplada del proyecto, es indispensable configurar el parámetro `submodules: 'recursive'`. Esta directiva instruye al agente para que descargue e integre de manera automática el repositorio y código de `evmaudit` dentro de la estructura de directorios del pipeline.

2.  **Autenticación en el Registro de Contenedores (GHCR):** Mediante la acción `docker/login-action@v2`, el pipeline establece una conexión segura con el registro oficial de GitHub (`ghcr.io`). El proceso se autentica de forma dinámica utilizando el actor del ciclo de vida (`${{ github.actor }}`) y un token de acceso seguro almacenado de forma cifrada en los secretos del repositorio bajo la clave `${{ secrets.IMAGES_TFM_UNIR }}`.

3.  **Normalización del Espacio de Nombres y Doble Etiquetado (*Multi-tagging*):** Las especificaciones de Docker y el estándar de la Open Container Initiative (OCI) prohíben estrictamente el uso de caracteres en mayúscula para los nombres de las imágenes de contenedores. Para solucionar esto, el pipeline ejecuta un script en Bash que convierte dinámicamente el nombre del repositorio a minúsculas utilizando el comando `tr '[:upper:]' '[:lower:]'`. Posteriormente, se implementa una estrategia de doble etiquetado para optimizar la trazabilidad y la inmutabilidad:
	- **Etiqueta por SHA (**`IMAGE_SHA`**):** Vincula de forma unívoca el contenedor con el hash del *commit* específico de Git que originó la compilación (`${{ github.sha }}`). Esto permite realizar auditorías retrospectivas y despliegues deterministas en caso de fallos.
    - **Etiqueta de Última Versión (**`IMAGE_LATEST`**):** Sobrescribe el puntero `:latest` con la versión más reciente del software que haya superado la fase de construcción con éxito.

4.  **Construcción y *Push* Multiplataforma:** Se invoca de manera directa el comando `docker build`, forzando la compilación bajo la arquitectura destino `--platform linux/amd64` utilizando el `Dockerfile` del proyecto como plano de construcción. Una vez generadas las imágenes locales con sus respectivas etiquetas, se ejecutan las instrucciones de empuje (*push*) hacia el registro seguro de GitHub, quedando el artefacto disponible para su consumo.


### ANEXO F.2.2.	Trabajo de Despliegue (deploy) y Limitaciones del Entorno

Para garantizar una separación formal de conceptos en la arquitectura de la integración, el pipeline implementa un segundo trabajo secuencial denominado `deploy`. Utilizando la directiva `needs: create-docker-image`, se establece una restricción de dependencia estricta: esta etapa no puede inicializarse si el empaquetado y la publicación previa de la imagen en el registro han fallado.

En la fase actual del proyecto, **esta etapa automatizada no ha sido implementada de forma activa y opera estrictamente como un punto de anclaje (*placeholder*) arquitectónico**. La justificación de esta decisión de diseño radica en las limitaciones técnicas del entorno de alojamiento seleccionado para las pruebas de concepto. La infraestructura de EVMAudit se despliega externamente en la plataforma PaaS **Railway** utilizando su modalidad de suscripción gratuita. Este nivel de servicio impone restricciones en las interfaces de programación (APIs) y en el uso de *webhooks*, impidiendo la ejecución de despliegues totalmente automatizados (*Automated CD Triggers*) desencadenados de forma directa mediante agentes de terceros como GitHub Actions.

Por consiguiente, el flujo de trabajo en este punto se limita a verificar la integridad de la secuencia de comandos en consola, quedando el aprovisionamiento de la infraestructura supeditado a los mecanismos nativos de la plataforma de destino. En el **siguiente apartado (X.5. Despliegue de la Infraestructura)**, se expondrá de manera más amplia la configuración, el aprovisionamiento y las características operativas de dicho entorno en Railway.

\newpage


# ANEXO G.	DESPLIEGUE DE LA INFRAESTRUCTURA EN LA NUBE (RAILWAY) 

Para validar la operatividad de EVMAudit en un entorno accesible y simular un escenario de producción real, se ha procedido al despliegue de la arquitectura contenedorizada en la plataforma de Plataforma como Servicio (PaaS) **Railway**. A continuación, se detallan las especificaciones del entorno, las restricciones técnicas de hardware identificadas y las optimizaciones de ingeniería aplicadas en el código fuente para garantizar la estabilidad del sistema.

## ANEXO G.1.  Aprovisionamiento y Configuración del Entorno Cloud

El proceso de despliegue en la infraestructura de la nube se ha estructurado bajo las siguientes directrices operativas:

- **Selección del Nivel de Servicio:** La instancia se ha instanciado haciendo uso del nivel gratuito (*Free Tier*) de la plataforma, el cual provee un crédito base de \$5 USD o un límite temporal de 30 días de cómputo.

- **Aislamiento Regional:** Con el objetivo de minimizar la latencia de red en las peticiones HTTP y optimizar la transferencia de datos, se ha seleccionado la región europea con nodo central en **Ámsterdam (EU)**.

- **Mapeo de Infraestructura y Orquestación:** El aprovisionamiento se realiza directamente vinculando el contenedor web a la imagen Docker compilada y almacenada en el registro de GitHub (ghcr.io), exponiendo de manera transparente la API del *backend* desarrollada en FastAPI.

- **Enrutamiento y Capa de Enlace (SSL):** La plataforma genera de manera dinámica un nombre de dominio completamente cualificado (FQDN) provisto de seguridad criptográfica TLS/SSL (HTTPS) para el acceso público a la interfaz de usuario: <https://evmaudit-production.up.railway.app/>.

## ANEXO G.2.  Limitaciones de Hardware y el Problema del Desbordamiento de Memoria (OOM)

La modalidad gratuita de la plataforma PaaS impone restricciones estrictas sobre los recursos de hardware asignados a cada contenedor, parametrizados de la siguiente forma:

- **Capacidad de Cómputo (CPU):** 2 vCPU virtuales compartidas.
- **Memoria Volátil (RAM):** 1 GB con un límite estricto de cuota (*Plan Limit*).

Bajo un escenario de despliegue convencional en servidores dedicados o infraestructura local, el pipeline de análisis de EVMAudit se ejecuta sin restricciones debido a la disponibilidad de memoria elástica. Sin embargo, en el entorno de la nube restringido, el motor de *fuzzing* basado en propiedades **Echidna** presenta un problema crítico de arquitectura.

Echidna, al estar desarrollado en Haskell, requiere de forma nativa una reserva inicial y un espacio de intercambio que supera con creces el gigabyte de memoria RAM para gestionar el mapa de cobertura del binario y la generación de casos de prueba. Al alcanzar el umbral crítico de 1 GB asignado por Railway, el demonio del sistema operativo anfitrión (*Kernel Out-of-Memory Killer*) destruía de manera abrupta el contenedor para salvaguardar la integridad del nodo, provocando la caída del servicio web y reportando un error de tipo *OOM*.

## ANEXO G.3.  Optimización del Sistema en Tiempo de Ejecución (RTS) de Haskell
Para mitigar el desbordamiento de memoria sin alterar las capacidades
analíticas esenciales de la herramienta, se realizó una intervención a
nivel de código en el módulo de control del *pipeline* (run_echidna). La
solución consistió en inyectar directivas específicas orientadas a
reconfigurar los parámetros del **Runtime System (RTS)** del compilador
de Glasgow Haskell (GHC) empaquetados dentro del binario de Echidna.

La estructura de invocación del proceso fue modificada e implementada en
Python mediante el siguiente diseño de argumentos:

```python
command = [
    "echidna",
    contract_path,
    "--contract", contract_name,
    "--format", "json",
    
    # Reducción del espacio de búsqueda del Fuzzer
    "--test-limit", "100",  
    
    # Optimización de la compilación inicial
    "--solc-args", "--optimize-runs 0", 
    
    # Apertura de las opciones del Runtime System de Haskell
    "+RTS",      
    
    # Parámetros estrictos de control de memoria y concurrencia
    "-M950m",    
    "-c",        
    "-N1",       
    
    # Cierre de las opciones RTS
    "-RTS"       
]
```
A continuación se expone la justificación técnica detrás de los modificadores inyectados:

- **Restricción de Ensayos (\--test-limit 100):** Al parametrizar el límite de pruebas en 100 iteraciones, se acota la profundidad del grafo de ejecución generado por el fuzzer. Esto reduce el consumo de memoria acumulativo a lo largo del tiempo de computación.
- **Techo Infranqueable de Memoria (-M950m):** Esta directiva establece que el asignador de memoria de Haskell tiene prohibido estrictamente reclamar más de 950 megabytes del espacio de usuario. Al situar este límite ligeramente por debajo del gigabyte real de Railway, se evita que el sistema operativo de la nube elimine el proceso por exceder la cuota física.
- **Recolección de Basura Agresiva (-c):** Activa un algoritmo de recolección de residuos más severo en el recolector de basura de Haskell (*Garbage Collector*). En lugar de acumular objetos intermedios en la memoria RAM, el sistema libera los recursos obsoletos inmediatamente después de cada evaluación de propiedad.
- **Concurrencia Confinada (-N1):** Limita la ejecución del entorno de ejecución a un único hilo de procesamiento, evitando la duplicación de estructuras de datos en memoria asociadas al paralelismo de hilos nativos.

Es importante destacar que la optimización descrita no se integró d forma estática en la construcción del archivo Dockerfile (lo que habrí alterado el comportamiento de la imagen base de manera permanente), sin que se aplicó directamente sobre el código fuente desplegado en el
contenedor en ejecución (*runtime*). Bajo condiciones de despliegue convencionales en infraestructuras con escalabilidad elástica o recurso dedicados de hardware, esta intervención técnica resultaría completamente innecesaria, ya que la aplicación contaría con la memoria suficiente para procesar el *pipeline* por defecto. Por consiguiente, esta modificación responde de manera estricta a un mecanismo de mitigación ad hoc, implementado exclusivamente para sortear las limitaciones físicas del entorno gratuito y evitar la interrupción forzada del servicio web por falta de memoria.

**Conclusión del Despliegue:** La implementación de estas salvaguardas de bajo nivel ha permitido que la aplicación web de **EVMAudit** opere de manera completamente estable y fluida en la nube. Pese a las severas restricciones del entorno gratuito de Railway, el sistema es capaz de completar con éxito el pipeline completo de auditoría en siete pasos sin registrar caídas en el servicio ni excepciones por falta de recursos.


\newpage


