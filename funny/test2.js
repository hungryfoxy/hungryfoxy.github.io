let make_cat = document.getElementById("make-cat");
let get_cat = document.getElementById("get-cat");

let count = 1;

function produce_cat() {
    let source = "./" + count + ".jpg";

    let cat_img = document.createElement("img");
    cat_img.setAttribute("src", source);
    cat_img.setAttribute("title", "cat " + count);
    cat_img.width = "200";
    cat_img.height = "200";
    make_cat.append(cat_img);

    count++;
}

get_cat.addEventListener("click", (event) => {
    if (count <= 5) {
        produce_cat();
    }

})