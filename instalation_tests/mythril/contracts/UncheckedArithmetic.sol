// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract UnsafeCounter {
    uint256 public counter;

    function increment(uint256 amount) external {
        unchecked { counter += amount; }
    }

    function decrement(uint256 amount) external {
        unchecked { counter -= amount; }
    }
}

contract EchidnaTest is UnsafeCounter {

    // Esta propiedad siempre es verdadera (trivial)
    function echidna_counter_no_underflow() public view returns (bool) {
        return counter <= type(uint256).max;
    }

    // Esta propiedad DEBE ser violada por el overflow
    function echidna_counter_stays_bounded() public view returns (bool) {
        return counter < 2**128;
    }
}
