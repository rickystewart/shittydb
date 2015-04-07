Public Module Test
    Sub Main()
        Dim sVal As String
        Call ShittyDBSet("foo", "literally faster than pure assembly")
        sVal = ShittyDBGet("foo")
        Console.WriteLine(sVal)
    End Sub
End Module
