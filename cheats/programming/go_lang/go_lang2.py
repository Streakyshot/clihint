cheats = [
    {
        "command": "go func()",
        "description": "Start a goroutine (lightweight thread)",
        "example": "go func() { fmt.Println(\"hi\") }()"
    },
    {
        "command": "channel := make(chan int)",
        "description": "Create a Go channel to sync goroutines",
        "example": "ch := make(chan string)"
    },
    {
        "command": "select { ... }",
        "description": "Wait on multiple channel operations",
        "example": "select { case msg := <-ch: fmt.Println(msg) }"
    },
    {
        "command": "defer",
        "description": "Schedule a function to run after the current one",
        "example": "defer fmt.Println(\"done\")"
    }
]
