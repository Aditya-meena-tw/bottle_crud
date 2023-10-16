<!DOCTYPE html>
<html>
<head>
    <title>Edit Names</title>
</head>
<body>
    <h1>Edit Names</h1>
    <form action="/edit/{{index}}" method="post">
        <input type="text" name="name" value="{{item}}" required>
        <input type="submit" value="Save">
    </form>
</body>
</html>
