import React, { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import { Text } from 'react-native-paper';

const pontos = [
  'Entrada Frente', 'Entrada Trás',
  '101', '102', '103', '104', '105', '106',
  '201', '202', '203', '204', '205', '206',
  '301', '302', '303', '304', '305', '306',
  'Banheiro 1', 'Banheiro 2',
  'Lanchonete', 'Web Class'
];

export default function Home() {
  const [origem, setOrigem] = useState('');
  const [destino, setDestino] = useState('');

  return (
    <View style={styles.container}>
      <Text variant="titleLarge">Escolha os pontos:</Text>
{/* 
      <Select
        data={pontos}
        onSelect={(selectedItem) => setOrigem(selectedItem)}
        defaultButtonText="Ponto de Origem"
        buttonStyle={styles.dropdown}
      />

      <Select
        data={pontos}
        onSelect={(selectedItem) => setDestino(selectedItem)}
        defaultButtonText="Ponto de Destino"
        buttonStyle={styles.dropdown}
      /> */}

      <Text variant="bodyLarge">Origem: {origem}</Text>
      <Text variant="bodyLarge">Destino: {destino}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    justifyContent: 'center',
  },
  dropdown: {
    width: '100%',
    marginVertical: 10,
    borderRadius: 8,
  },
});
