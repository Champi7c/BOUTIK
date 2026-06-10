/* ============================================
   BRIGHT LOOKS — JavaScript Principal
   ============================================ */

document.addEventListener('DOMContentLoaded', function () {

  // ===== DARK MODE TOGGLE =====
  const darkToggle = document.getElementById('darkToggle');
  darkToggle?.addEventListener('click', () => {
    const html = document.documentElement;
    const isDark = html.getAttribute('data-theme') === 'dark';
    const next = isDark ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    darkToggle.innerHTML = next === 'dark' ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
  });

  // ===== NAVBAR SCROLL =====
  const navbar = document.querySelector('.navbar');
  window.addEventListener('scroll', () => {
    navbar?.classList.toggle('scrolled', window.scrollY > 50);
  });

  // ===== HAMBURGER MENU =====
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  hamburger?.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileMenu?.classList.toggle('active');
    document.body.style.overflow = mobileMenu?.classList.contains('active') ? 'hidden' : '';
  });

  // ===== SEARCH BAR =====
  const searchToggle = document.getElementById('searchToggle');
  const searchBar = document.getElementById('searchBar');
  const searchInput = document.getElementById('searchInput');
  const searchResults = document.getElementById('searchResults');

  searchToggle?.addEventListener('click', () => {
    searchBar?.classList.toggle('active');
    if (searchBar?.classList.contains('active')) searchInput?.focus();
  });

  document.addEventListener('click', (e) => {
    if (!searchBar?.contains(e.target) && e.target !== searchToggle) {
      searchBar?.classList.remove('active');
    }
  });

  let searchTimeout;
  searchInput?.addEventListener('input', (e) => {
    clearTimeout(searchTimeout);
    const q = e.target.value.trim();
    if (q.length < 2) { searchResults.style.display = 'none'; return; }
    searchTimeout = setTimeout(() => {
      fetch(`/recherche/?q=${encodeURIComponent(q)}`, {
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
      })
      .then(r => r.json())
      .then(data => {
        if (data.results.length === 0) {
          searchResults.innerHTML = '<div style="padding:1rem;color:#888;font-size:.85rem;">Aucun résultat</div>';
        } else {
          searchResults.innerHTML = data.results.map(p => `
            <a href="${p.url}" class="search-result-item">
              <img src="${p.image}" alt="${p.name}" class="search-result-img" onerror="this.src='/static/images/placeholder.jpg'">
              <div>
                <div class="search-result-name">${p.name}</div>
                <div class="search-result-price">${formatPrice(p.price)} FCFA</div>
              </div>
            </a>
          `).join('');
        }
        searchResults.style.display = 'block';
      });
    }, 300);
  });

  // ===== CART AJAX =====
  document.addEventListener('click', function (e) {
    const addBtn = e.target.closest('[data-add-cart]');
    if (!addBtn) return;
    e.preventDefault();

    const productId = addBtn.dataset.productId;
    const size = document.querySelector('.size-btn.selected')?.dataset.size || '';
    const color = document.querySelector('.color-btn.selected')?.dataset.color || '';
    const qty = parseInt(document.querySelector('.qty-input')?.value || 1);

    fetch('/panier/ajouter/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
        'X-Requested-With': 'XMLHttpRequest',
      },
      body: JSON.stringify({ product_id: productId, quantity: qty, size, color })
    })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        updateCartBadge(data.cart_count);
      }
    });
  });

  // ===== CART REMOVE AJAX =====
  document.addEventListener('click', function (e) {
    const removeBtn = e.target.closest('[data-remove-cart]');
    if (!removeBtn) return;
    e.preventDefault();

    const key = removeBtn.dataset.key;
    fetch('/panier/supprimer/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
        'X-Requested-With': 'XMLHttpRequest',
      },
      body: JSON.stringify({ key })
    })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        document.querySelector(`[data-cart-row="${key}"]`)?.remove();
        updateCartBadge(data.cart_count);
        updateCartTotal(data.cart_total);
        if (data.cart_count === 0) location.reload();
      }
    });
  });

  // ===== CART QTY UPDATE =====
  document.addEventListener('change', function (e) {
    const qtyInput = e.target.closest('[data-cart-qty]');
    if (!qtyInput) return;

    const key = qtyInput.dataset.key;
    const quantity = parseInt(qtyInput.value);

    fetch('/panier/modifier/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
        'X-Requested-With': 'XMLHttpRequest',
      },
      body: JSON.stringify({ key, quantity })
    })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        updateCartBadge(data.cart_count);
        updateCartTotal(data.cart_total);
        const subtotal = document.querySelector(`[data-item-total="${key}"]`);
        if (subtotal) subtotal.textContent = formatPrice(data.item_total) + ' FCFA';
      }
    });
  });

  // ===== SIZE SELECTOR =====
  document.querySelectorAll('.size-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.size-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
    });
  });

  // ===== COLOR SELECTOR =====
  document.querySelectorAll('.color-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.color-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
    });
  });

  // ===== QTY SELECTOR =====
  const qtyMinus = document.getElementById('qtyMinus');
  const qtyPlus = document.getElementById('qtyPlus');
  const qtyInput = document.querySelector('.qty-input');

  qtyMinus?.addEventListener('click', () => {
    const v = parseInt(qtyInput.value);
    if (v > 1) qtyInput.value = v - 1;
  });
  qtyPlus?.addEventListener('click', () => {
    const v = parseInt(qtyInput.value);
    qtyInput.value = v + 1;
  });

  // ===== PRODUCT IMAGES =====
  document.querySelectorAll('.product-thumbnail').forEach(thumb => {
    thumb.addEventListener('click', () => {
      const mainImg = document.querySelector('.product-main-img img');
      if (mainImg) {
        mainImg.src = thumb.querySelector('img').src;
        document.querySelectorAll('.product-thumbnail').forEach(t => t.classList.remove('active'));
        thumb.classList.add('active');
      }
    });
  });

  // ===== WISHLIST AJAX =====
  document.addEventListener('click', function (e) {
    const wishBtn = e.target.closest('[data-wishlist]');
    if (!wishBtn) return;
    e.preventDefault();

    const productId = wishBtn.dataset.productId;
    fetch(`/favoris/toggle/${productId}/`, {
      headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
    .then(r => r.json())
    .then(data => {
      wishBtn.classList.toggle('wishlisted', data.action === 'added');
      const icon = wishBtn.querySelector('i');
      if (icon) {
        icon.className = data.action === 'added' ? 'fas fa-heart' : 'far fa-heart';
      }
    });
  });

  // ===== DELIVERY TYPE =====
  const deliveryRadios = document.querySelectorAll('[name="delivery_type"]');
  const addressField = document.getElementById('deliveryAddressField');
  deliveryRadios.forEach(radio => {
    radio.addEventListener('change', () => {
      if (addressField) {
        addressField.style.display = radio.value === 'livraison' ? 'block' : 'none';
      }
    });
  });

  // ===== PAYMENT OPTION SELECTION =====
  document.querySelectorAll('.payment-option').forEach(opt => {
    opt.addEventListener('click', () => {
      document.querySelectorAll('.payment-option').forEach(o => o.classList.remove('selected'));
      opt.classList.add('selected');
      opt.querySelector('input[type="radio"]').checked = true;
    });
  });

  // ===== LAZY LOADING =====
  if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[data-src]');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.classList.add('loaded');
          observer.unobserve(img);
        }
      });
    }, { rootMargin: '200px' });
    lazyImages.forEach(img => observer.observe(img));
  }

  // ===== DISMISS MESSAGES =====
  document.querySelectorAll('.alert-dismiss').forEach(btn => {
    btn.addEventListener('click', () => btn.closest('.alert')?.remove());
  });
  setTimeout(() => {
    document.querySelectorAll('.messages-container .alert').forEach(el => {
      el.style.opacity = '0';
      el.style.transition = 'opacity 0.5s';
      setTimeout(() => el.remove(), 500);
    });
  }, 4000);

  // ===== SORT PRODUCTS =====
  const sortSelect = document.getElementById('sortSelect');
  sortSelect?.addEventListener('change', () => {
    const url = new URL(window.location);
    url.searchParams.set('tri', sortSelect.value);
    window.location = url.toString();
  });

  // ===== SCROLL TO TOP =====
  const scrollTop = document.getElementById('scrollTop');
  window.addEventListener('scroll', () => {
    scrollTop?.classList.toggle('visible', window.scrollY > 400);
  });
  scrollTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

});

// ===== HELPERS =====
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function formatPrice(price) {
  return parseInt(price).toLocaleString('fr-FR');
}

function updateCartBadge(count) {
  document.querySelectorAll('.cart-badge').forEach(b => {
    b.textContent = count;
    b.style.display = count > 0 ? 'flex' : 'none';
  });
}

function updateCartTotal(total) {
  const el = document.getElementById('cartTotal');
  if (el) el.textContent = formatPrice(total) + ' FCFA';
}
