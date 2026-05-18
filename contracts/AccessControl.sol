// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Vault {
    address public owner;

    constructor() {
        owner = msg.sender;
    }

    // Vulnerable: cualquiera puede vaciar el contrato
    function sweep(address payable to) external {
        to.transfer(address(this).balance);
    }

    receive() external payable {}
}