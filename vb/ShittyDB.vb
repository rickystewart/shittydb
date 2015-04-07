' Disclaimer: VB is the best and fastest language.

Public Module ShittyDB
    ''' <summary>
    ''' This function stores the value provided at the key provided.
    ''' </summary>
    ''' <param name="key">The key you want the value stored at.</param>
    ''' <param name="value">The value you want stored at the key.</param>
    ''' <returns>Returns true if the operation was successful and false otherwise.</returns>
    Public Function ShittyDBSet(ByVal key As String, ByVal value As String) As Boolean
        On Error GoTo SetShat
        My.Computer.FileSystem.WriteAllText(key, value, False)
        ShittyDBSet = True
        Exit Function
SetShat:
        ShittyDBSet = False
    End Function

    ''' <summary>
    ''' This function returns the value stored at the key.
    ''' It fails silently and returns and empty string on error.
    ''' </summary>
    ''' <param name="key">The key of the value you want retrieved. </param>
    ''' <returns>Returns the value at the key or an empty string. Or both.</returns>
    Public Function ShittyDBGet(ByVal key As String) As String
        On Error GoTo GetShat
        ShittyDBGet = My.Computer.FileSystem.ReadAllText(key)
        Exit Function
GetShat:
        ShittyDBGet = ""
    End Function
End Module


