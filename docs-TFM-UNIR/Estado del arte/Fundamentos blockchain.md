
# 1. Fundamentos de la tecnología blockchain

## 1.1. Origen y concepto de la tecnología blockchain

El término _blockchain_ se refiere a una tecnología de registro distribuido (_Distributed Ledger Technology_, DLT) que alcanzó notoriedad con la aparición de Bitcoin en 2009, propuesto por Satoshi Nakamoto [1]. En esencia, una blockchain es una base de datos compartida y replicada entre múltiples nodos de una red _peer-to-peer_ (P2P), cuyo objetivo es mantener un historial secuencial e inmutable de transacciones agrupadas en bloques [2].

Cada bloque contiene un conjunto de transacciones validadas, una marca temporal y una referencia criptográfica al bloque anterior, normalmente en forma de _hash_, formando así una cadena cronológica que preserva la integridad del historial [3]. Este encadenamiento criptográfico hace extremadamente difícil modificar la información ya confirmada, puesto que cualquier alteración en un bloque invalidaría el enlace con los bloques posteriores.

La propuesta de Nakamoto resolvió uno de los problemas clásicos de los sistemas distribuidos abiertos, esto es, cómo alcanzar confianza entre entidades que no confían entre sí. En lugar de depender de una autoridad central, el libro mayor es mantenido de forma cooperativa por los participantes de la red, lo que dota al sistema de propiedades como descentralización, inmutabilidad relativa, transparencia y resistencia a la censura [4].

Estas características distinguen a blockchain de los sistemas tradicionales de gestión de datos y permiten realizar transacciones seguras entre pares sin necesidad de intermediarios de confianza. Durante la última década, el concepto de blockchain ha evolucionado más allá de Bitcoin y se ha convertido en la base tecnológica de múltiples plataformas descentralizadas. Aunque la literatura ofrece distintas definiciones y alcances del término [5], [6], todas coinciden en varios elementos fundamentales: la existencia de un registro distribuido, la protección criptográfica frente a manipulaciones y la cooperación entre nodos bajo reglas de consenso.

En consecuencia, blockchain puede entenderse como un mecanismo _trustless_, en el que la veracidad de las transacciones no depende de la autoridad de una entidad central, sino de pruebas criptográficas y del consenso colectivo [7]. Este enfoque ha impulsado un notable interés académico, industrial e institucional, consolidando a blockchain como una de las tecnologías disruptivas más relevantes en ámbitos como las finanzas, la identidad digital y la ciberseguridad [8].

---

## 1.2. Estructura y componentes de una cadena de bloques

En una blockchain, la información se organiza en bloques enlazados secuencialmente mediante técnicas criptográficas. De forma general, cada bloque se compone de una cabecera (_header_) y un cuerpo de transacciones. La cabecera incluye, entre otros campos, el _hash_ del bloque anterior, la marca temporal y una raíz criptográfica que resume las transacciones incluidas en el bloque [3].

El uso de funciones _hash_ criptográficas, como SHA-256 en Bitcoin, proporciona integridad al sistema, ya que cualquier modificación en los datos de un bloque altera su resumen criptográfico y rompe la continuidad de la cadena. Además, muchas implementaciones emplean árboles de Merkle para organizar internamente las transacciones [9]. Esta estructura permite calcular una raíz única que representa el conjunto completo de transacciones y posibilita verificar de forma eficiente la pertenencia de una transacción concreta sin necesidad de procesar el bloque entero.

Esta propiedad resulta especialmente relevante para mecanismos de verificación ligera, como _Simplified Payment Verification_ (SPV), donde nodos con recursos limitados pueden comprobar la inclusión de transacciones consultando únicamente las rutas de _hashes_ pertinentes. En consecuencia, el árbol de Merkle refuerza tanto la integridad como la consistencia de los datos almacenados [9].

Otro componente esencial es la propia transacción, que representa una operación registrada en la red, como una transferencia de valor o la invocación de un contrato inteligente. Las transacciones son firmadas digitalmente por su emisor utilizando criptografía asimétrica y posteriormente propagadas por la red hasta ser incorporadas a un bloque válido. Una vez que dicho bloque se añade a la cadena, las transacciones incluidas pasan a considerarse confirmadas.

La combinación del encadenamiento entre bloques, la replicación distribuida y la protección criptográfica hace que el historial almacenado sea resistente a manipulaciones. Modificar o eliminar registros pasados implicaría rehacer todos los bloques posteriores y, además, imponer esa versión modificada sobre una porción suficiente de la red, lo cual resulta computacionalmente inviable bajo los supuestos de seguridad del sistema. Esta propiedad aporta una elevada capacidad de trazabilidad y auditoría, si bien también implica un crecimiento continuo del historial almacenado.

---

## 1.3. Funcionamiento de la red blockchain

El funcionamiento de una blockchain se apoya en una red descentralizada de nodos interconectados que comparten y actualizan el libro mayor conforme a un protocolo común. El proceso comienza cuando un usuario genera una transacción, la firma digitalmente y la transmite a la red P2P. A continuación, los nodos la propagan hasta alcanzar a aquellos responsables de agrupar transacciones en bloques.

En redes abiertas o _permissionless_, como Bitcoin o Ethereum, cualquier nodo puede participar en la validación y propuesta de bloques, siempre que cumpla las reglas del protocolo. Las transacciones pendientes se almacenan temporalmente en la _mempool_. De forma periódica, un validador selecciona un conjunto de transacciones válidas y construye un bloque candidato.

Antes de ser añadido a la cadena, dicho bloque debe satisfacer las condiciones impuestas por el mecanismo de consenso. Dependiendo del protocolo, esto puede implicar resolver un problema criptográfico, ser seleccionado en función del capital bloqueado o completar una ronda de votación distribuida. Una vez validado, el bloque se difunde al resto de la red, cuyos nodos comprueban su corrección verificando tanto las transacciones incluidas como su referencia al bloque anterior.

Si el bloque es correcto, se incorpora a la copia local del ledger de cada nodo. De esta forma, la red va sincronizando progresivamente una visión común del historial. Aunque pueden producirse bifurcaciones temporales, por ejemplo, si dos nodos generan bloques válidos casi simultáneamente, el protocolo de consenso garantiza que la red converge finalmente hacia una única secuencia aceptada por la mayoría [3].

Este modelo proporciona tolerancia frente a fallos bizantinos, permitiendo mantener la coherencia del registro incluso en presencia de nodos maliciosos o defectuosos, siempre que una fracción suficiente de participantes actúe honestamente. En suma, la red blockchain opera como un sistema cooperativo y descentralizado en el que la integridad del historial se mantiene mediante verificación criptográfica y consenso, sin necesidad de autoridad central [10].

---

## 1.4. Algoritmos de consenso distribuidos

El consenso constituye el núcleo técnico que permite a los nodos de una blockchain acordar un historial único de transacciones válidas. Existen múltiples algoritmos de consenso, diseñados para responder a distintos requisitos de seguridad, rendimiento y gobernanza.

En las cadenas públicas, las dos familias más relevantes son _Proof of Work_ (PoW) y _Proof of Stake_ (PoS). En PoW, utilizado originalmente en Bitcoin, los nodos validadores compiten por resolver un problema criptográfico difícil, generalmente consistente en encontrar un _hash_ por debajo de un umbral de dificultad [11]. El primer nodo que encuentra una solución válida obtiene el derecho a proponer el siguiente bloque y recibe una recompensa asociada. Este mecanismo aporta seguridad al hacer costosa la reescritura de la cadena, aunque implica un elevado consumo energético y una limitada escalabilidad.

Como alternativa, PoS selecciona validadores en función de la cantidad de activos bloqueados como garantía dentro de la red [12]. En este modelo, la seguridad se basa en incentivos económicos: si un validador actúa de manera deshonesta, puede perder parte de sus fondos mediante mecanismos de penalización o _slashing_ [13]. Este enfoque reduce significativamente el coste energético y mejora el tiempo de finalización, aunque introduce nuevos retos, como la concentración de poder o determinados ataques económicos.

Además de PoW y PoS, la literatura recoge múltiples variantes y enfoques híbridos, entre ellos _Proof of Authority_ (PoA), _Delegated Proof of Stake_ (DPoS) y protocolos basados en tolerancia a fallos bizantinos (_Byzantine Fault Tolerance_, BFT), especialmente frecuentes en redes permissionadas [14]. La elección de un algoritmo de consenso condiciona de forma directa tanto la resistencia frente a ataques como las prestaciones del sistema en términos de latencia, rendimiento y consumo de recursos.

---

## 1.5. Tipos de redes blockchain: públicas, privadas e híbridas

Las redes blockchain pueden clasificarse según el grado de apertura, control de acceso y gobernanza [15]. En una blockchain pública o _permissionless_, cualquier usuario puede unirse a la red, leer el historial de transacciones y, en función del protocolo, participar en la validación de bloques. Bitcoin y Ethereum constituyen ejemplos paradigmáticos de este modelo. Estas redes priorizan la descentralización y la resistencia a la censura, aunque a costa de menores tasas de rendimiento y mayor consumo de recursos.

Por el contrario, las blockchains privadas o _permissioned_ restringen la participación a entidades autorizadas. En ellas, el conjunto de nodos validadores se encuentra previamente definido, lo que permite mejorar la velocidad, reducir el coste computacional y reforzar el control sobre la privacidad de los datos [16]. Hyperledger Fabric es uno de los ejemplos más representativos de este enfoque.

Entre ambos extremos se sitúan las redes híbridas o de consorcio, donde varias organizaciones comparten la gobernanza y validación del sistema. Este modelo busca equilibrar transparencia, eficiencia y control institucional [17]. La elección entre uno u otro tipo de red depende en gran medida del caso de uso, del nivel de confianza entre participantes y de los requisitos regulatorios, de privacidad y de escalabilidad.

---

## 1.6. Fundamentos criptográficos y seguridad de los datos

La seguridad de blockchain se apoya en varias primitivas criptográficas fundamentales. En primer lugar, las funciones _hash_ criptográficas se utilizan para enlazar bloques y resumir transacciones. Estas funciones son deterministas, resistentes a preimagen y altamente sensibles a cualquier modificación en la entrada, lo que las convierte en una herramienta esencial para garantizar la integridad del sistema [18].

En segundo lugar, la criptografía de clave pública permite autenticar transacciones mediante firmas digitales. En redes como Bitcoin y Ethereum, es habitual el uso de ECDSA sobre la curva secp256k1 para verificar que una transacción ha sido autorizada por el propietario legítimo de una clave privada. De este modo, la red puede garantizar autenticidad y no repudio sin necesidad de exponer la clave secreta del emisor.

Asimismo, estructuras como los árboles de Merkle permiten resumir grandes volúmenes de datos y verificar su pertenencia de forma eficiente. Sobre esta base, algunas plataformas incorporan además técnicas criptográficas avanzadas, como pruebas de conocimiento cero, firmas agregadas o mecanismos de ocultación de importes y destinatarios.

No obstante, la fortaleza de la arquitectura no depende exclusivamente de la robustez de las primitivas criptográficas, sino también de su correcta implementación. Vulnerabilidades derivadas de una gestión deficiente de claves, errores en la generación de nonces o software cliente inseguro pueden comprometer la seguridad del ecosistema, incluso si el protocolo subyacente es sólido [18].

---

## 1.7. Contratos inteligentes y programación en blockchain

Uno de los principales avances posteriores a Bitcoin fue la incorporación de contratos inteligentes, esto es, programas desplegados y ejecutados sobre la propia blockchain [19]. Aunque el concepto fue formulado originalmente por Nick Szabo, fue Ethereum quien lo materializó de forma generalista al proporcionar un entorno de ejecución cuasi Turing-completo basado en la _Ethereum Virtual Machine_ (EVM) [20].

En este modelo, los contratos se programan en lenguajes como Solidity, se compilan a _bytecode_ y se almacenan en el estado global de la cadena. Cada contrato dispone de una dirección propia y puede ser invocado mediante transacciones enviadas por usuarios u otros contratos. Su ejecución es determinista y replicada por todos los nodos validadores, lo que permite verificar públicamente el comportamiento del sistema [21].

Para evitar abusos computacionales, Ethereum incorpora un mecanismo de _gas_ que asigna un coste a cada operación ejecutada por la EVM [22]. De este modo, cada transacción debe aportar recursos suficientes para cubrir su ejecución, lo que previene bucles infinitos y limita el impacto de ataques de denegación de servicio.

Los contratos inteligentes han dado lugar a un amplio ecosistema de aplicaciones descentralizadas, incluyendo tokens, plataformas DeFi, mercados de NFT, sistemas de votación, identidad digital y servicios automatizados [23], [24]. Sin embargo, la inmutabilidad del código desplegado convierte cualquier error lógico o vulnerabilidad en un riesgo crítico, especialmente cuando el contrato administra activos de alto valor.

---

## 1.8. Vulnerabilidades y amenazas a la seguridad en blockchain

A pesar de sus garantías criptográficas y distribuidas, blockchain no está exenta de vulnerabilidades. Las amenazas pueden clasificarse en diferentes niveles [25], [26].

En primer lugar, existen vulnerabilidades asociadas al usuario y al cliente, como el robo de claves privadas, la gestión insegura de credenciales o errores en la generación de firmas digitales [27], [28]. En segundo lugar, se encuentran los ataques dirigidos al mecanismo de consenso, entre los que destaca el ataque del 51 %, mediante el cual un actor con control mayoritario sobre la capacidad de validación puede reorganizar la cadena y facilitar dobles gastos [29].

También se han estudiado ataques específicos sobre infraestructuras de minería, como _selfish mining_, _block withholding_ o estrategias de soborno para alterar el orden de las transacciones [30]. A nivel de red, resultan relevantes los ataques Sybil, eclipse y DDoS, que buscan aislar nodos, manipular su visión del sistema o degradar la disponibilidad de la red [31], [32].

En la capa de aplicación, los contratos inteligentes constituyen hoy uno de los principales focos de riesgo. Vulnerabilidades como reentrancia, errores de control de acceso o fallos lógicos han sido explotadas en incidentes de gran impacto económico, como el ataque a The DAO [33]. La creciente composicionalidad del ecosistema DeFi también ha ampliado la superficie de ataque, especialmente en puentes entre cadenas, oráculos y protocolos interconectados [34], [35].

Aunque se han propuesto contramedidas para mitigar muchos de estos riesgos, la seguridad en blockchain sigue siendo un ámbito en continua evolución. La complejidad técnica, la exposición pública del código y la presión económica del entorno hacen imprescindible combinar robustez criptográfica, diseño seguro del consenso, auditoría de contratos y buenas prácticas operativas [36], [37].

---

## 1.9. Escalabilidad y rendimiento

Uno de los principales retos de las blockchains públicas es la escalabilidad. Al requerir que un gran número de nodos valide cada transacción, estos sistemas suelen presentar menor rendimiento que las bases de datos centralizadas. Bitcoin, por ejemplo, procesa aproximadamente siete transacciones por segundo, mientras que Ethereum, en su capa base, mantiene un rendimiento de apenas unas decenas de transacciones por segundo.

Esta limitación responde a decisiones de diseño orientadas a preservar la seguridad y la descentralización. Aumentar el tamaño de los bloques o reducir drásticamente el tiempo entre ellos puede incrementar el rendimiento, pero también elevar el riesgo de bifurcaciones, los requisitos de red y el grado de centralización [38], [39].

Para abordar este problema se han propuesto diversas soluciones. Entre ellas destacan el _sharding_, que divide la carga de procesamiento entre subconjuntos de nodos [40], y las soluciones de segunda capa, como Lightning Network o los _rollups_, que desplazan parte del cómputo y almacenamiento fuera de la cadena principal [41], [42]. Estas estrategias persiguen mejorar la capacidad transaccional sin comprometer en exceso las garantías de seguridad del sistema base.

---

## 1.10. Privacidad y protección de datos en blockchain

Las blockchains públicas priorizan la transparencia, ya que todas las transacciones quedan registradas en un libro mayor accesible públicamente [43]. Aunque las identidades se representan mediante direcciones pseudónimas, la trazabilidad de las operaciones puede facilitar la inferencia de información sensible.

Para mitigar esta limitación, se han desarrollado diversas técnicas orientadas a preservar la privacidad. Monero, por ejemplo, utiliza firmas de anillo, direcciones furtivas y transacciones confidenciales para ocultar origen, destino e importe [44], [45]. Zcash, por su parte, emplea pruebas de conocimiento cero para validar transacciones sin revelar sus detalles [46].

Más allá de las criptomonedas orientadas a la privacidad, las pruebas de conocimiento cero se están extendiendo a identidades descentralizadas, verificación selectiva de atributos y soluciones de escalabilidad. No obstante, la privacidad en blockchain sigue siendo un problema abierto, especialmente por el conflicto entre inmutabilidad, transparencia y regulaciones sobre protección de datos [47], [48].

---

## 1.11. Tendencias actuales y desafíos futuros

En el horizonte de 2026, blockchain se encuentra en una fase de maduración acelerada. Su adopción en sectores empresariales, institucionales y financieros ha ido acompañada del desarrollo de nuevos casos de uso, como finanzas descentralizadas, identidad digital, trazabilidad y automatización contractual [8].

Entre los desafíos más relevantes destacan la interoperabilidad entre cadenas, la mejora de la gobernanza descentralizada, la escalabilidad sostenible y la protección frente a amenazas emergentes. En particular, la computación cuántica plantea un riesgo potencial para los algoritmos criptográficos empleados actualmente en blockchain [49]. Aunque dicho riesgo no es inmediato, ya se investigan estrategias de migración hacia esquemas poscuánticos [50], [51].

En paralelo, organismos internacionales y marcos regulatorios están avanzando en la estandarización de términos, procesos de seguridad e interoperabilidad. Todo ello sugiere que el futuro de blockchain dependerá no solo de su robustez técnica, sino también de su capacidad para integrarse en entornos regulados, interoperables y con garantías reforzadas de privacidad y ciberseguridad.

---

# Referencias

[1] A. S. Rajasekaran, M. Azees, and F. Al-Turjman, “A comprehensive survey on blockchain technology,” _Sustainable Energy Technologies and Assessments_, vol. 52, Art. 102039, 2022. doi: 10.1016/j.seta.2022.102039.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911](https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911)

[2] L. M. Saldaña Trejo, G. Gallegos García, and R. Aldeco Pérez, “Protocolos criptográficos de consenso en blockchain para el Internet de las Cosas,” _Computación y Sistemas_, vol. 29, no. 2, pp. 643–657, 2025. doi: 10.13053/CyS-29-2-5694.  
Disponible en: https://www.researchgate.net/publication/395964329_Protocolos_criptograficos_de_consenso_en_blockchain_para_el_Internet_de_las_cosas

[3] Z. Wu, H. Xu, M. Yue, and Y. Lu, “Blockchain security threats: A comprehensive classification and impact assessment,” _Computer Networks_, vol. 265, Art. 111284, 2025. doi: 10.1016/j.comnet.2025.111284.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X](https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X)

[4] EU Blockchain Observatory and Forum, _Ethereum Merge Trend Report_, Apr. 2023.  
Disponible en: [https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl](https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl)

[5] M. H. Tabatabaei, R. Vitenberg, and N. R. Veeraragavan, “Understanding blockchain: definitions, architecture, design, and system comparison,” _Computer Science Review_, vol. 50, Art. 100575, 2023. doi: 10.1016/j.cosrev.2023.100575.  
Disponible en: [https://ar5iv.labs.arxiv.org/html/2207.02264](https://ar5iv.labs.arxiv.org/html/2207.02264)

[6] A. Guru, B. K. Mohanta, H. Mohapatra, F. Al-Turjman, C. Altrjman, and A. Yadav, “A Survey on Consensus Protocols and Attacks on Blockchain Technology,” _Applied Sciences_, vol. 13, no. 4, Art. 2604, 2023. doi: 10.3390/app13042604.  
Disponible en: [https://www.mdpi.com/2076-3417/13/4/2604](https://www.mdpi.com/2076-3417/13/4/2604)

[7] P. De Filippi, C. Wray, and G. Sileno, “Smart contracts,” _Internet Policy Review_, vol. 10, no. 2, 2021. doi: 10.14763/2021.2.1549.  
Disponible en: [https://policyreview.info/glossary/smart-contracts](https://policyreview.info/glossary/smart-contracts)

[8] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[9] L. M. Saldaña Trejo, G. Gallegos García, and R. Aldeco Pérez, “Protocolos criptográficos de consenso en blockchain para el Internet de las Cosas,” _Computación y Sistemas_, vol. 29, no. 2, pp. 643–657, 2025. doi: 10.13053/CyS-29-2-5694.  
Disponible en: [https://cys.cic.ipn.mx/index.php/CyS/article/download/5694/3961](https://cys.cic.ipn.mx/index.php/CyS/article/download/5694/3961)

[10] Z. Wu, H. Xu, M. Yue, and Y. Lu, “Blockchain security threats: A comprehensive classification and impact assessment,” _Computer Networks_, vol. 265, Art. 111284, 2025. doi: 10.1016/j.comnet.2025.111284.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X](https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X)

[11] EU Blockchain Observatory and Forum, _Ethereum Merge Trend Report_, Apr. 2023.  
Disponible en: [https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl](https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl)

[12] EU Blockchain Observatory and Forum, _Ethereum Merge Trend Report_, Apr. 2023.  
Disponible en: [https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl](https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl)

[13] EU Blockchain Observatory and Forum, _Ethereum Merge Trend Report_, Apr. 2023.  
Disponible en: [https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl](https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl)

[14] A. Guru _et al_., “A Survey on Consensus Protocols and Attacks on Blockchain Technology,” _Applied Sciences_, vol. 13, no. 4, Art. 2604, 2023. doi: 10.3390/app13042604.  
Disponible en: [https://www.mdpi.com/2076-3417/13/4/2604](https://www.mdpi.com/2076-3417/13/4/2604)

[15] M. H. Tabatabaei, R. Vitenberg, and N. R. Veeraragavan, “Understanding blockchain: definitions, architecture, design, and system comparison,” _Computer Science Review_, vol. 50, Art. 100575, 2023. doi: 10.1016/j.cosrev.2023.100575.  
Disponible en: [https://ar5iv.labs.arxiv.org/html/2207.02264](https://ar5iv.labs.arxiv.org/html/2207.02264)

[16] M. H. Tabatabaei, R. Vitenberg, and N. R. Veeraragavan, “Understanding blockchain: definitions, architecture, design, and system comparison,” _Computer Science Review_, vol. 50, Art. 100575, 2023. doi: 10.1016/j.cosrev.2023.100575.  
Disponible en: [https://ar5iv.labs.arxiv.org/html/2207.02264](https://ar5iv.labs.arxiv.org/html/2207.02264)

[17] M. H. Tabatabaei, R. Vitenberg, and N. R. Veeraragavan, “Understanding blockchain: definitions, architecture, design, and system comparison,” _Computer Science Review_, vol. 50, Art. 100575, 2023. doi: 10.1016/j.cosrev.2023.100575.  
Disponible en: [https://ar5iv.labs.arxiv.org/html/2207.02264](https://ar5iv.labs.arxiv.org/html/2207.02264)

[18] A. Guru _et al_., “A Survey on Consensus Protocols and Attacks on Blockchain Technology,” _Applied Sciences_, vol. 13, no. 4, Art. 2604, 2023. doi: 10.3390/app13042604.  
Disponible en: [https://www.mdpi.com/2076-3417/13/4/2604](https://www.mdpi.com/2076-3417/13/4/2604)

[19] P. De Filippi, C. Wray, and G. Sileno, “Smart contracts,” _Internet Policy Review_, vol. 10, no. 2, 2021. doi: 10.14763/2021.2.1549.  
Disponible en: [https://policyreview.info/glossary/smart-contracts](https://policyreview.info/glossary/smart-contracts)

[20] P. De Filippi, C. Wray, and G. Sileno, “Smart contracts,” _Internet Policy Review_, vol. 10, no. 2, 2021. doi: 10.14763/2021.2.1549.  
Disponible en: [https://policyreview.info/glossary/smart-contracts](https://policyreview.info/glossary/smart-contracts)

[21] P. De Filippi, C. Wray, and G. Sileno, “Smart contracts,” _Internet Policy Review_, vol. 10, no. 2, 2021. doi: 10.14763/2021.2.1549.  
Disponible en: [https://policyreview.info/glossary/smart-contracts](https://policyreview.info/glossary/smart-contracts)

[22] M. H. Tabatabaei, R. Vitenberg, and N. R. Veeraragavan, “Understanding blockchain: definitions, architecture, design, and system comparison,” _Computer Science Review_, vol. 50, Art. 100575, 2023. doi: 10.1016/j.cosrev.2023.100575.  
Disponible en: [https://ar5iv.labs.arxiv.org/html/2207.02264](https://ar5iv.labs.arxiv.org/html/2207.02264)

[23] P. De Filippi, C. Wray, and G. Sileno, “Smart contracts,” _Internet Policy Review_, vol. 10, no. 2, 2021. doi: 10.14763/2021.2.1549.  
Disponible en: [https://policyreview.info/glossary/smart-contracts](https://policyreview.info/glossary/smart-contracts)

[24] P. De Filippi, C. Wray, and G. Sileno, “Smart contracts,” _Internet Policy Review_, vol. 10, no. 2, 2021. doi: 10.14763/2021.2.1549.  
Disponible en: [https://policyreview.info/glossary/smart-contracts](https://policyreview.info/glossary/smart-contracts)

[25] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[26] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[27] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[28] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[29] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[30] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[31] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[32] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[33] Z. Wu, H. Xu, M. Yue, and Y. Lu, “Blockchain security threats: A comprehensive classification and impact assessment,” _Computer Networks_, vol. 265, Art. 111284, 2025. doi: 10.1016/j.comnet.2025.111284.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X](https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X)

[34] Z. Wu, H. Xu, M. Yue, and Y. Lu, “Blockchain security threats: A comprehensive classification and impact assessment,” _Computer Networks_, vol. 265, Art. 111284, 2025. doi: 10.1016/j.comnet.2025.111284.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X](https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X)

[35] Z. Wu, H. Xu, M. Yue, and Y. Lu, “Blockchain security threats: A comprehensive classification and impact assessment,” _Computer Networks_, vol. 265, Art. 111284, 2025. doi: 10.1016/j.comnet.2025.111284.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X](https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X)

[36] Z. Wu, H. Xu, M. Yue, and Y. Lu, “Blockchain security threats: A comprehensive classification and impact assessment,” _Computer Networks_, vol. 265, Art. 111284, 2025. doi: 10.1016/j.comnet.2025.111284.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X](https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X)

[37] Z. Wu, H. Xu, M. Yue, and Y. Lu, “Blockchain security threats: A comprehensive classification and impact assessment,” _Computer Networks_, vol. 265, Art. 111284, 2025. doi: 10.1016/j.comnet.2025.111284.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X](https://www.sciencedirect.com/science/article/abs/pii/S138912862500252X)

[38] A. S. Rajasekaran, M. Azees, and F. Al-Turjman, “A comprehensive survey on blockchain technology,” _Sustainable Energy Technologies and Assessments_, vol. 52, Art. 102039, 2022. doi: 10.1016/j.seta.2022.102039.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911](https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911)

[39] A. S. Rajasekaran, M. Azees, and F. Al-Turjman, “A comprehensive survey on blockchain technology,” _Sustainable Energy Technologies and Assessments_, vol. 52, Art. 102039, 2022. doi: 10.1016/j.seta.2022.102039.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911](https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911)

[40] A. S. Rajasekaran, M. Azees, and F. Al-Turjman, “A comprehensive survey on blockchain technology,” _Sustainable Energy Technologies and Assessments_, vol. 52, Art. 102039, 2022. doi: 10.1016/j.seta.2022.102039.  
Disponible en: [https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911](https://www.sciencedirect.com/science/article/abs/pii/S2213138822000911)

[41] EU Blockchain Observatory and Forum, _Ethereum Merge Trend Report_, Apr. 2023.  
Disponible en: [https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl](https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl)

[42] EU Blockchain Observatory and Forum, _Ethereum Merge Trend Report_, Apr. 2023.  
Disponible en: [https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl](https://blockchain-observatory.ec.europa.eu/document/download/3f78c885-d14e-47cb-b183-f22ef529a258_en?filename=EUBOF3.0_Ethereum_Merge_Trend_Report_final.pdf&prefLang=sl)

[43] A. Alfaw, W. Elmedany, and M. S. Sharif, “Blockchain Vulnerabilities and Recent Security Challenges: A Review Paper,” in _Proc. 2022 Int. Conf. Data Analytics for Business and Industry (ICDABI)_, 2022, pp. 780–786. doi: 10.1109/ICDABI56818.2022.10041611.  
Disponible en: [https://uel-repository.worktribe.com/OutputFile/440701](https://uel-repository.worktribe.com/OutputFile/440701)

[44] “Monero Privacy Explained: Ring Signatures, Stealth Addresses, RingCT,” _Monero How_.  
Disponible en: [https://www.monero.how/tutorial-monero-privacy-ring-signatures-stealth-addresses-ringct](https://www.monero.how/tutorial-monero-privacy-ring-signatures-stealth-addresses-ringct)

[45] “Monero Reaches New Record as Privacy Takes Center Stage,” _Coinfomania_.  
Disponible en: [https://coinfomania.com/monero-reaches-new-record-as-privacy-takes-center-stage/](https://coinfomania.com/monero-reaches-new-record-as-privacy-takes-center-stage/)

[46] “A Survey of Blockchain-Based Privacy Applications,” arXiv, 2024.  
Disponible en: [https://arxiv.org/html/2411.16404v1](https://arxiv.org/html/2411.16404v1)

[47] L. M. Saldaña Trejo, G. Gallegos García, and R. Aldeco Pérez, “Protocolos criptográficos de consenso en blockchain para el Internet de las Cosas,” _Computación y Sistemas_, vol. 29, no. 2, pp. 643–657, 2025. doi: 10.13053/CyS-29-2-5694.  
Disponible en: [https://cys.cic.ipn.mx/index.php/CyS/article/download/5694/3961](https://cys.cic.ipn.mx/index.php/CyS/article/download/5694/3961)

[48] “A Survey of Blockchain-Based Privacy Applications,” arXiv, 2024.  
Disponible en: [https://arxiv.org/html/2411.16404v1](https://arxiv.org/html/2411.16404v1)

[49] H. Khodaiemehr, K. Bagheri, and C. Feng, “Navigating the quantum computing threat landscape for blockchains: A comprehensive survey,” _Computer Science Review_, vol. 59, Art. 100846, 2026. doi: 10.1016/j.cosrev.2025.100846.  
Disponible en: [https://www.sciencedirect.com/science/article/pii/S1574013725001224](https://www.sciencedirect.com/science/article/pii/S1574013725001224)

[50] H. Khodaiemehr, K. Bagheri, and C. Feng, “Navigating the quantum computing threat landscape for blockchains: A comprehensive survey,” _Computer Science Review_, vol. 59, Art. 100846, 2026. doi: 10.1016/j.cosrev.2025.100846.  
Disponible en: [https://www.sciencedirect.com/science/article/pii/S1574013725001224](https://www.sciencedirect.com/science/article/pii/S1574013725001224)

[51] H. Khodaiemehr, K. Bagheri, and C. Feng, “Navigating the quantum computing threat landscape for blockchains: A comprehensive survey,” _Computer Science Review_, vol. 59, Art. 100846, 2026. doi: 10.1016/j.cosrev.2025.100846.  
Disponible en: [https://www.sciencedirect.com/science/article/pii/S1574013725001224](https://www.sciencedirect.com/science/article/pii/S1574013725001224)
