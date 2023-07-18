from models import Post, User


admin_user = User(
    username="toddthebod",
    password="Password123lmao",
    email="todd@example.com",
    first_name="Todd",
    last_name="Birchard",
    bio="I write tutorials on the internet.",
    avatar_url="https://storage.googleapis.com/hackersandslackers-cdn/authors/todd_small@2x.jpg",
    role="admin",
)

post_1 = Post(
    author_id=1,
    slug="fake-post-slug",
    title="Fake Post Title",
    status="published",
    summary="A fake post to have some fake comments.",
    feature_image="https://cdn.hackersandslackers.com/2021/01/logo-smaller@2x.png",
    body="Cheese slices monterey jack cauliflower cheese dolcelatte cheese and wine fromage frais rubber cheese gouda. Rubber cheese cheese and wine cheeseburger cheesy grin paneer paneer taleggio caerphilly.  Edam mozzarella.",
)

post_2 = Post(
    author_id=1,
    slug="an-additional-post",
    title="Yet Another Post Title",
    status="published",
    summary="An in-depth exploration into writing your second blog post.",
    feature_image="https://cdn.hackersandslackers.com/2021/01/logo-smaller@2x.png",
    body="Smelly cheese cheese slices fromage. Pepper jack taleggio monterey jack cheeseburger pepper jack swiss everyone loves. Cheeseburger say cheese brie fromage frais swiss when the cheese comes out everybody's happy babybel cheddar. Cheese and wine cheesy grin",
)