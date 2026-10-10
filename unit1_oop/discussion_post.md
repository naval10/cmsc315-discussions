# Initial Discussion Post Draft

GitHub repository: https://github.com/naval10/cmsc315-discussions

## Design Approach

I used a home-network example for my implementation. `ParentClass` represented a general network device, and `ChildClass` represented a firewall. Each object stored its own name, location, and configuration. The firewall inherited the basic device setup and added rule management. I used `__str__()` for readable output and `__len__()` to return the number of rules. The `rules` property returned a tuple snapshot, while methods validated changes to the internal list. My extension allowed a rule to be removed safely.

## Reflection

This assignment helped me understand inheritance, namespaces, and the difference between shallow and deep copying. My example connected to the home network I use daily. Encapsulation resembled managing a device through its settings interface without needing to know every internal detail. Inheritance let my firewall reuse general device information while adding specialized behavior.

The main challenge in this implementation was avoiding shared configuration changes when an independent copy was needed. I addressed this by comparing shallow and deep copies and checking their nested data. A shallow copy shared the rule list, while a deep copy preserved an independent configuration. I also tested invalid and duplicate rules. Catching these errors allowed the demonstration to continue and accept a later valid rule, turning an invalid operation into a manageable issue instead of a program failure.

Compared with procedural programming, OOP required more setup but kept related data and behavior together. Reusing parent methods reduced repetition and made future changes easier. For my cybersecurity interests, this approach could support cloud monitoring or connected-device management. I would balance that flexibility against memory overhead, especially when storing many devices or copying large configurations.

## Memory and Reliability

The rule list used O(n) storage for n rules of bounded length. Duplicate checks and removals took O(n) time. Deep copying required additional storage for independent mutable data. For a larger application, I would consider a set alongside the list to speed up duplicate checks while preserving rule order.

How did you decide when shared data was acceptable and when your objects needed independent copies?
