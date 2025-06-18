document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.getAttribute('data-product-id');
            fetch(`/add-to-cart/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(data.message); // Показываем сообщение
                    console.log('Товаров в корзине:', data.count);
                } else {
                    alert('Ошибка при добавлении в корзину');
                }
            })
            .catch(error => console.error('Ошибка:', error));
        });
    });
});