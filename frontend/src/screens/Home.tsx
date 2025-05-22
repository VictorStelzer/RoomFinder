import React, { useState } from 'react';
import { View, StyleSheet, ScrollView, Alert, Modal, TouchableOpacity, FlatList, TouchableWithoutFeedback } from 'react-native';
import { Text, Card, Divider, TextInput, Button, Checkbox } from 'react-native-paper';
import api from '../services/api';

type Ponto = string;

type Passo = {
  from: string;
  direction: string;
  distance: number;
  to: string;
};

type CaminhoResponse = {
  caminho_formatado: string[];
  distancia_total: string;
  detalhes: {
    caminho: Array<[string, string | null, number]>;
    distancia: number;
  };
};

const pontos: Ponto[] = [
  'EntradaFrontal', 'EntradaTraseira',
  'Sala101', 'Sala102', 'Sala103', 'Sala104', 'Sala105', 'Sala106',
  'Sala201', 'Sala202', 'Sala203', 'Sala204', 'Sala205', 'Sala206',
  'Sala301', 'Sala302', 'Sala303', 'Sala304', 'Sala305', 'Sala306',
  'Banheiro1A', 'Banheiro1B', 'Banheiro2A', 'Banheiro2B',
  'Lanchonete', 'WebClass'
];

const CustomSelect = ({
  value,
  items,
  placeholder,
  onSelect,
}: {
  value: string;
  items: string[];
  placeholder: string;
  onSelect: (item: string) => void;
}) => {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <TouchableOpacity onPress={() => setVisible(true)}>
        <TextInput
          mode="outlined"
          value={value}
          placeholder={placeholder}
          editable={false}
          right={<TextInput.Icon icon="chevron-down" />}
          style={styles.selectInput}
        />
      </TouchableOpacity>

      <Modal
        visible={visible}
        transparent
        animationType="slide"
        onRequestClose={() => setVisible(false)}>
        <TouchableWithoutFeedback onPress={() => setVisible(false)}>
          <View style={styles.modalOverlay}>
            <TouchableWithoutFeedback>
              <View style={styles.modalContent}>
                <FlatList
                  data={items}
                  keyExtractor={(item) => item}
                  renderItem={({ item }) => (
                    <TouchableOpacity
                      style={styles.selectItem}
                      onPress={() => {
                        onSelect(item);
                        setVisible(false);
                      }}>
                      <Text>{item}</Text>
                    </TouchableOpacity>
                  )}
                  ItemSeparatorComponent={() => <Divider />}
                />
              </View>
            </TouchableWithoutFeedback>
          </View>
        </TouchableWithoutFeedback>
      </Modal>
    </>
  );
};

export default function Home() {
  const [origem, setOrigem] = useState<Ponto>('');
  const [destino, setDestino] = useState<Ponto>('');
  const [caminho, setCaminho] = useState<CaminhoResponse | null>(null);
  const [mostrarCaminho, setMostrarCaminho] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [acessibilidade, setAcessibilidade] = useState<boolean>(false);

  const buscarCaminho = async () => {
    if (!origem || !destino) return;

    setLoading(true);
    try {
      const response = await api.get<CaminhoResponse>('/caminho', {
        params: { 
          origem, 
          destino,
          acessibilidade: acessibilidade ? 'true' : undefined
        },
      });
      setCaminho(response.data);
      setMostrarCaminho(true);
    } catch (error) {
      console.error('Erro:', error);
      Alert.alert('Erro', 'Não foi possível encontrar o caminho. Verifique os pontos selecionados.');
      setMostrarCaminho(false);
    } finally {
      setLoading(false);
    }
  };

  const parsePasso = (passo: string): Passo => {
    const match = passo.match(/Vá de \((.*?)\) até \((.*?)\)/);
    if (!match) return { from: '', direction: '', distance: 0, to: '' };

    const [from, direction, distance] = match[1].split(',').map(s => s.trim().replace(/'/g, ''));
    const to = match[2].split(',')[0].trim().replace(/'/g, '');

    return {
      from,
      direction: direction || 'siga em frente',
      distance: parseInt(distance) || 0,
      to
    };
  };

  return (
    <ScrollView style={styles.container}>
      <Text variant="titleLarge" style={styles.title}>RoomFinder</Text>
      <Text style={styles.subtitle}>Encontre o melhor caminho no campus</Text>

      <CustomSelect
        value={origem}
        items={pontos}
        placeholder="Selecione a origem"
        onSelect={(item) => setOrigem(item)}
      />

      <CustomSelect
        value={destino}
        items={pontos}
        placeholder="Selecione o destino"
        onSelect={(item) => setDestino(item)}
      />

      <View style={styles.checkboxContainer}>
        <Checkbox
          status={acessibilidade ? 'checked' : 'unchecked'}
          onPress={() => setAcessibilidade(!acessibilidade)}
          color="#6200ee"
        />
        <Text style={styles.checkboxLabel}>Preciso de rota acessível (usar rampa)</Text>
      </View>

      <Button 
        mode="contained" 
        onPress={buscarCaminho}
        disabled={!origem || !destino || loading}
        loading={loading}
        style={styles.buscarButton}
        labelStyle={styles.buscarButtonLabel}
      >
        {loading ? "Buscando..." : "Buscar caminho"}
      </Button>

      {mostrarCaminho && caminho && (
        <Card style={styles.card}>
          <Card.Title
            title="Caminho Encontrado"
            titleStyle={styles.cardTitle}
            subtitle={`Distância total: ${caminho.distancia_total}`}
            subtitleStyle={styles.cardSubtitle}
          />
          <Card.Content>
            <ScrollView style={styles.scrollView}>
              {caminho.caminho_formatado.map((passo, index) => {
                const { from, direction, distance, to } = parsePasso(passo);
                return (
                  <View key={index} style={styles.passoContainer}>
                    <Text style={styles.passoNumero}>{index + 1}.</Text>
                    <View style={styles.passoContent}>
                      <Text style={styles.passoTexto}>
                        De <Text style={styles.local}>{from}</Text>
                      </Text>
                      <Text style={styles.passoTexto}>
                        Vire <Text style={styles.direcao}>{direction.toLowerCase()}</Text> ({distance}m)
                      </Text>
                      <Text style={styles.passoTexto}>
                        Para <Text style={styles.local}>{to}</Text>
                      </Text>
                    </View>
                  </View>
                );
              })}
            </ScrollView>
          </Card.Content>
        </Card>
      )}
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f5f5',
  },
  title: {
    textAlign: 'center',
    marginBottom: 5,
    color: '#6200ee',
    fontWeight: 'bold',
  },
  subtitle: {
    textAlign: 'center',
    marginBottom: 20,
    color: '#666',
  },
  picker: {
    backgroundColor: 'white',
    marginVertical: 10,
    borderRadius: 5,
  },
  card: {
    marginTop: 20,
    elevation: 3,
    borderRadius: 8,
  },
  cardTitle: {
    fontWeight: 'bold',
  },
  cardSubtitle: {
    color: '#6200ee',
  },
  scrollView: {
    maxHeight: 300,
  },
  passoContainer: {
    flexDirection: 'row',
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  passoNumero: {
    fontWeight: 'bold',
    marginRight: 8,
    color: '#6200ee',
  },
  passoContent: {
    flex: 1,
  },
  passoTexto: {
    marginBottom: 2,
    color: '#333',
  },
  local: {
    fontWeight: 'bold',
    color: '#333',
  },
  direcao: {
    color: '#6200ee',
    textTransform: 'lowercase',
  },
  selectInput: {
    backgroundColor: 'white',
    marginVertical: 10,
  },
  modalOverlay: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: 'rgba(0,0,0,0.5)',
    width: '100%', 
    height: '100%', 
  },
  modalContent: {
    backgroundColor: 'white',
    marginHorizontal: 20,
    borderRadius: 8,
    maxHeight: '60%',
  },
  selectItem: {
    padding: 15,
  },
  buscarButton: {
    marginTop: 10,
    backgroundColor: '#6200ee',
  },
  buscarButtonLabel: {
    color: 'white',
  },
  checkboxContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginVertical: 10,
  },
  checkboxLabel: {
    marginLeft: 8,
    color: '#333',
  },
});