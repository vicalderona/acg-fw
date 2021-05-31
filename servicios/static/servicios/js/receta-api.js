$(document).ready(function() {
    $.getJSON('https://www.themealdb.com/api/json/v1/1/random.php', function(data) {
        var receta = data;

        $.each(receta.meals, function(i, item) {
            $("#nombre").html('<h3>Nombre: </h3> ' + item.strMeal);
            $("#img").html("<img src='" + item.strMealThumb + "'>");
            $("#categoria").html('<h3>Categoria: </h3>  ' + item.strCategory);
            $("#origen").html('<h3>Origen: </h3>  ' + item.strArea);
            $("#ingredientes").html('<h3>Ingredientes: </h3>  ' + item.strIngredient1 + ' ' +
                item.strIngredient2 + ' ' + item.strIngredient3 + ' ' + item.strIngredient4 + ' ' +
                item.strIngredient5 + ' ' + item.strIngredient6 + ' ' + item.strIngredient7 + ' ' +
                item.strIngredient8 + ' ' + item.strIngredient9 + ' ' + item.strIngredient10 + ' ' +
                item.strIngredient11 + ' ' + item.strIngredient12 + ' ' + item.strIngredient13 + ' ' +
                item.strIngredient14 + ' ' + item.strIngredient15 + ' ' + item.strIngredient16 + ' ' +
                item.strIngredient17 + ' ' + item.strIngredient18 + ' ' + item.strIngredient19 + ' ' +
                item.strIngredient20);
            $("#pasos").html('<h3>Instrucciones: </h3> ' + item.strInstructions);
            $("#video").html("<a href= '" + item.strYoutube + "'>Video instructivo</a>");
        })



    })
})