
# 1. Fundamentos de Blockchain

## 1.1. Concepto base

Una blockchain puede definirse como una **estructura de datos enlazada por bloques**, donde cada bloque contiene un conjunto de transacciones o eventos junto con metadatos que permiten verificar su integridad. El encadenamiento se produce porque cada bloque incorpora una referencia criptográfica al bloque anterior, generalmente mediante una función hash, lo que genera una secuencia de estados difícil de modificar retrospectivamente [1][2].

Desde una perspectiva de ciberseguridad, el interés de blockchain no reside únicamente en su descentralización, sino en que sustituye la confianza en una autoridad central por una combinación de:

- Criptografía
- Replicación distribuida
- Validación colectiva
- Reglas de consenso
- Trazabilidad de estados

Este cambio de paradigma ha sido ampliamente analizado en la literatura, donde se describe blockchain como una **máquina de estados replicada en un entorno adversarial** [3].

---

## 1.2. Estructura de un bloque

Aunque existen variaciones según la implementación, un bloque suele contener:

- **Cabecera**
    - hash del bloque previo
    - marca temporal
    - raíz criptográfica (Merkle root)
    - parámetros del consenso
    
- **Cuerpo**
    - lista de transacciones o instrucciones
    
- **Metadatos adicionales**
    - firma
    - nonce
    - identificadores del productor del bloque

El uso de funciones hash criptográficas es fundamental, ya que permiten garantizar la integridad del sistema. Una función hash transforma una entrada arbitraria en una salida de longitud fija, y sus propiedades de resistencia a colisiones y efecto avalancha permiten detectar manipulaciones [1].

Tal y como señala NIST, los hashes constituyen una de las primitivas esenciales sobre las que se construye la seguridad de blockchain [1].

---

## 1.3. Libro mayor distribuido

A diferencia de una base de datos centralizada, en blockchain el estado se replica entre múltiples nodos de una red peer-to-peer. Cada nodo mantiene una copia del ledger o una representación suficiente para validar el estado global.

Este modelo aporta:
- Redundancia
- Resistencia a fallos
- Dificultad de manipulación unilateral
- Auditabilidad

Sin embargo, es importante destacar que esto no implica seguridad absoluta. La seguridad depende del modelo de amenaza, del mecanismo de consenso y de la distribución real del poder entre participantes [4].

En términos académicos, blockchain no elimina la confianza, sino que la redistribuye hacia el protocolo, los incentivos y la mayoría honesta.

---

## 1.4. Consenso distribuido

El problema fundamental que resuelve blockchain es cómo lograr que nodos potencialmente deshonestos acuerden un estado común del sistema. Este acuerdo se consigue mediante mecanismos de consenso distribuido.

### Proof of Work (PoW)

En PoW, los nodos compiten resolviendo problemas computacionales costosos. El derecho a proponer el siguiente bloque depende del esfuerzo computacional realizado. Este modelo dificulta la manipulación, ya que reescribir la historia requiere rehacer el trabajo acumulado [2][4].

No obstante, presenta limitaciones importantes en términos de eficiencia energética y escalabilidad [5].

### Proof of Stake (PoS)

En PoS, el derecho a validar bloques depende del capital bloqueado (_stake_) por los participantes. Ethereum ha adoptado este modelo, donde los validadores pueden ser penalizados económicamente por comportamientos maliciosos.

Desde un punto de vista técnico, PoS reduce el consumo energético, pero introduce nuevos vectores de ataque relacionados con incentivos económicos, como _long-range attacks_ o problemas de finalización [6].

---

## 1.5. Criptografía aplicada

Blockchain se fundamenta en varias primitivas criptográficas:

- Funciones hash → integridad y encadenamiento
- Criptografía asimétrica → identidad
- Firmas digitales → autenticación y no repudio
- Árboles de Merkle → eficiencia en verificación

Estas técnicas permiten verificar que una transacción ha sido autorizada por el propietario legítimo y que no ha sido alterada [1].

Sin embargo, la literatura reciente señala que muchas vulnerabilidades no derivan de la criptografía en sí, sino de su uso incorrecto en implementaciones software [3].

---

## 1.6. Modelo de estado

Existen dos modelos principales:

- **UTXO (Bitcoin)**
- **Modelo de cuentas (Ethereum)**

Ethereum distingue dos tipos de cuentas:

- Externally Owned Accounts (EOA)
- Contract accounts

Este modelo facilita la ejecución de lógica compleja y persistente, lo que ha permitido el desarrollo de smart contracts [7].

No obstante, también incrementa la superficie de ataque, al permitir la ejecución de código arbitrario en un entorno distribuido.

---

## 1.7. Ethereum Virtual Machine (EVM)

La ejecución de contratos inteligentes en Ethereum se realiza en la **Ethereum Virtual Machine (EVM)**, una máquina de pila determinista que ejecuta bytecode.

El Yellow Paper define la EVM como una máquina de estado formal cuasi Turing-completa [2]. Esta capacidad permite computación general, pero introduce riesgos significativos, ya que errores en el código pueden traducirse en vulnerabilidades explotables con impacto económico directo [8].

---

## 1.8. Gas y coste computacional

El gas es el mecanismo que mide el coste computacional en Ethereum. Cada operación tiene un coste asociado y cada transacción define un límite (`gasLimit`).

El gas cumple funciones críticas:

- Evita bucles infinitos
- Protege frente a abuso computacional
- Asigna coste económico a los recursos

Investigaciones recientes han demostrado que el modelo de gas puede ser explotado para ataques de denegación de servicio o _griefing_ [9].

---

## 1.9. Propiedades fundamentales

Las propiedades clave de blockchain incluyen:

- Descentralización
- Integridad
- Inmutabilidad relativa
- Trazabilidad
- Transparencia
- Resistencia a censura

Es importante matizar que la inmutabilidad no es absoluta, sino que depende de factores computacionales, económicos y sociales [1][4].

---

## 1.10. Smart contracts como extensión natural

Una blockchain programable permite desplegar **smart contracts**, programas que ejecutan lógica de negocio de forma determinista.

Su principal ventaja es la ejecución verificable y descentralizada. Sin embargo, su principal riesgo es que cualquier error queda permanentemente registrado y puede ser explotado, como demuestran numerosos ataques documentados en la literatura [3][8].

---

## 1.11. Limitaciones y visión crítica

Desde una perspectiva académica, blockchain presenta limitaciones relevantes:

- Baja escalabilidad
- Latencia elevada
- Alto coste de replicación
- Complejidad técnica
- Exposición pública del código
- Dificultad de actualización

Por ello, en ciberseguridad aplicada a smart contracts, el foco debe situarse en cómo estas propiedades amplifican el impacto de vulnerabilidades software, lo que justifica el desarrollo de herramientas avanzadas de análisis como la propuesta en este TFM.

---

# Referencias (IEEE con enlaces)

[1] NIST, _“Blockchain Technology Overview,”_ 2018.  
 [https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8202.pdf](https://nvlpubs.nist.gov/nistpubs/ir/2018/NIST.IR.8202.pdf)

[2] G. Wood, _“Ethereum Yellow Paper,”_ 2014.  
 [https://ethereum.github.io/yellowpaper/paper.pdf](https://ethereum.github.io/yellowpaper/paper.pdf)

[3] N. Atzei et al., _“A Survey of Attacks on Ethereum Smart Contracts,”_ Springer, 2017.  
 [https://doi.org/10.1007/978-3-662-54455-6_8](https://doi.org/10.1007/978-3-662-54455-6_8)

[4] A. Gervais et al., _“On the Security and Performance of Proof-of-Work Blockchains,”_ ACM CCS, 2016.  
[https://doi.org/10.1145/2976749.2978341](https://doi.org/10.1145/2976749.2978341)

[5] M. Conti et al., _“A Survey on Security and Privacy Issues of Bitcoin,”_ IEEE Communications Surveys & Tutorials, 2018.  
 [https://doi.org/10.1109/COMST.2018.2842460](https://doi.org/10.1109/COMST.2018.2842460)

[6] V. Buterin and V. Griffith, _“Casper the Friendly Finality Gadget,”_ arXiv, 2017.  
 [https://arxiv.org/abs/1710.09437](https://arxiv.org/abs/1710.09437)

[7] A. M. Antonopoulos and G. Wood, _Mastering Ethereum,_ 2018.  
[https://github.com/ethereumbook/ethereumbook](https://github.com/ethereumbook/ethereumbook)

[8] L. Luu et al., _“Making Smart Contracts Smarter,”_ ACM CCS, 2016.  
 [https://doi.org/10.1145/2976749.2978309](https://doi.org/10.1145/2976749.2978309)

[9] M. Rodler et al., _“Sereum,”_ NDSS, 2019.  
 [https://doi.org/10.14722/ndss.2019.23182](https://doi.org/10.14722/ndss.2019.23182)

