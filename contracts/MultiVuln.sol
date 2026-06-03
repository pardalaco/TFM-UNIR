// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MultiVuln {
    mapping(address => uint256) public balances;
    address public owner;

    constructor() { owner = msg.sender; }

    // SWC-107: Reentrancia — llamada externa antes de actualizar estado
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Saldo insuficiente");
        (bool ok,) = msg.sender.call{value: amount}("");
        require(ok, "Fallo al enviar");
        balances[msg.sender] -= amount;
    }

    // SWC-106: selfdestruct accesible por cualquiera
    function kill() external {
        selfdestruct(payable(msg.sender));
    }

    // SWC-115: tx.origin para autenticación (vulnerable a phishing)
    function adminAction() external {
        require(tx.origin == owner, "Not owner");
    }

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }
}
