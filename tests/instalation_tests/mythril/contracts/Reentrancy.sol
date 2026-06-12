// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract VulnerableBank {
    mapping(address => uint256) public balances;

    function deposit() external payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Saldo insuficiente");

        // Vulnerable: llamada externa ANTES de actualizar estado
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Fallo al enviar ether");

        balances[msg.sender] -= amount;
    }
}