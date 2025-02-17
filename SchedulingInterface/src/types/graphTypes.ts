export interface Node {
    id: string;
    label: string;
    rank: number;
    duration: number;
    early_date: number | null;
    late_date: number | null;
    total_margin: number | null;
    free_margin: number | null;
}

export interface Edge {
    from: string;
    to: string;
    label: string;
}

export interface Task {
    id: string;
    duration: number;
    dependencies: string[];
    early_dates: number;
    late_dates: number;
    total_margins: number;
    free_margins: number;
}

export interface GraphData {
    graph: {
        nodes: Node[];
        edges: Edge[];
    };
    tasks: Task[];
    matrix: number[][];
    ranks: { [key: string]: number };
    calendar: {
        early_dates: number[];
        late_dates: number[];
        total_margins: number[];
        free_margins: number[];
    };
    criticalPath: string[];
    hasCircuit: boolean;
    nodes: any[];
    edges: any[];
}

export interface GraphDisplayProps {
    data: GraphData;
    zoom: number;
    viewMode: 'timeline' | 'tree';
    showCriticalPath: boolean;
}

export type GraphResponse = GraphData;
