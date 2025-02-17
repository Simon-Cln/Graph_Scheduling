import { GraphData } from '../types/graphTypes';

export const fetchGraphData = async (file: File): Promise<GraphData> => {
    try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch('http://localhost:5000/api/upload', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Failed to fetch graph data');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching graph data:', error);
        throw error;
    }
};
