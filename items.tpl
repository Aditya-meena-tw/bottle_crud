
<!DOCTYPE html>
<html>
<head>
    <title>Name</title>
</head>
<body>
    <h1>Names</h1>
    <ul>
        %for i, item in enumerate(items):
            <li>
                {{item}} -
                <a href="/edit/{{i}}">Edit</a> |
                <a href="/delete/{{i}}">Delete</a>
            </li>
        %end
    </ul>
    <h2>Add New Names</h2>
    <form action="/add" method="post">
        <input type="text" name="name" required>
        <input type="submit" value="Add">
    </form>
</body>
</html>
