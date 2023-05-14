This is the packaging diagram representing the structure of the program:

[diagram]![diagram3](https://user-images.githubusercontent.com/128533486/232876533-cc95ea23-b095-4451-a537-5c66b3d9a1de.jpg)

This is the sequence diagram describing how to create a user. If there is not already a user with the same username, it works as follows:

```mermaid

    sequenceDiagram
        actor User
        User->>UI: press login button
        UI->>UserService: log_in(username), e.g. log_in("laura")
        UserService->>UserRepository: find_by_username("laura")
        UserRepository-->>UserService: user
        UserService-->>UI: user
        
```
        
