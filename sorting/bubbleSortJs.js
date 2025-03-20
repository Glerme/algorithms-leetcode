function bubble(arr) {
  let size = arr.length;

  for (let _ of arr) {
    let isSorted = true;
    console.log(arr);
    for (let i = 0; i < size - 1; i++) {
      if (arr[i] > arr[i + 1]) {
        isSorted = false;
        // Troca os elementos
        [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
      }
    }

    // Se o array estiver ordenado, podemos parar a execução
    if (isSorted) return;
  }
}

// Testando
bubble([5, 4, 3, 2, 1]);
bubble([1, 2, 3, 4, 5]);
