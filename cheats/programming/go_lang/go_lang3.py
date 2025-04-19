cheats = [
    {
        "command": "http.ListenAndServe",
        "description": "Start a simple HTTP server",
        "example": "http.ListenAndServe(\":8080\", nil)"
    },
    {
        "command": "json.NewEncoder(w).Encode(obj)",
        "description": "Return JSON from a Go API endpoint",
        "example": "json.NewEncoder(w).Encode(response)"
    },
    {
        "command": "http.Get(\"url\")",
        "description": "Perform an HTTP GET request",
        "example": "resp, err := http.Get(\"https://example.com\")"
    },
    {
        "command": "http.FileServer(http.Dir(\"./static\"))",
        "description": "Serve static files in Go",
        "example": "fs := http.FileServer(http.Dir(\"./static\"))"
    }
]
